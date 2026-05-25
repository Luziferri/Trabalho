import os
import secrets
import socket

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from models import db, User
from sqlalchemy import text

app = Flask(__name__)
app.config.from_object("settings") 
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or app.config.get('SECRET_KEY') or secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        existing_columns = {
            row[1]
            for row in db.session.execute(text("PRAGMA table_info('user')"))
        }
        colunas_necessarias = [
            'avatar', 'madeira', 'telhas', 'casas',
            'comida', 'joias', 'soldados', 'cavalos',
            'fazendas', 'estradas', 'castelos', 'portos', 'igrejas'
        ]

        for column_name in colunas_necessarias:
            if column_name == 'avatar':
                column_sql = "avatar TEXT NOT NULL DEFAULT 'default.png'"
            else:
                column_sql = f"{column_name} INTEGER NOT NULL DEFAULT 0"
            if column_name not in existing_columns:
                db.session.execute(text(f"ALTER TABLE user ADD COLUMN {column_sql}"))
        db.session.commit()


EDIFICIOS_INFO = {
    'casa': {'custo': {'madeira': 50, 'telhas': 50}, 'coluna': 'casas'},
    'fazenda': {'custo': {'comida': 10}, 'coluna': 'fazendas'},
    'estrada': {'custo': {'comida': 5}, 'coluna': 'estradas'},
    'castelo': {'custo': {'comida': 20, 'joias': 5}, 'coluna': 'castelos'},
    'porto': {'custo': {'comida': 15, 'joias': 2}, 'coluna': 'portos'},
    'igreja': {'custo': {'joias': 10}, 'coluna': 'igrejas'},
}

RECRUTAR_SOLDADOS_CUSTO = {'comida': 10, 'joias': 2}
RECRUTAR_SOLDADOS_GANHO = 5

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        dificuldade = request.form.get('dificuldade', 'Normal')
        pergunta = request.form.get('pergunta_seguranca', '')
        resposta = request.form.get('resposta_seguranca', '').strip().lower() # Guardar em minúsculas
        avatar_escolhido = request.form.get('avatar', 'default.png')
        
        if not username or not password or not email or not pergunta or not resposta:
            flash('Todos os campos são obrigatórios!', 'danger')
            return redirect(url_for('register'))
            
        existing_user = User.query.filter((User.username==username) | (User.email==email)).first()
        if existing_user:
            flash('Nome de utilizador ou email já em uso.', 'danger')
            return redirect(url_for('register'))
            
        # Criação do utilizador com os novos campos avançados teste 1 teste 2 teste 3 teste 4
        new_user = User(
            username=username, 
            email=email, 
            dificuldade=dificuldade,
            pergunta_seguranca=pergunta,
            resposta_seguranca=resposta,
            avatar=avatar_escolhido
        )
        new_user.set_password(password) # Usa o hashing reforçado
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Conta criada com sucesso! Já podes entrar.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Valida as credenciais e inicia a sessão local do utilizador."""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f'Olá, {user.username}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciais incorretas. Tenta novamente.', 'danger')
            
    return render_template('login.html')


@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar_password():
    """Sistema de recuperação de conta baseado em pergunta de segurança."""
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        resposta = request.form.get('resposta_seguranca', '').strip().lower()
        nova_password = request.form.get('nova_password', '')
        
        user = User.query.filter_by(username=username).first()
        
        # Verifica se o utilizador existe e se a resposta bate certo
        if user and user.resposta_seguranca == resposta:
            user.set_password(nova_password)
            db.session.commit()
            flash('A tua password foi reposta com sucesso! Podes fazer login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Nome de utilizador ou resposta de segurança incorretos.', 'danger')
            
    return render_template('recuperar.html')


@app.route('/perfil')
def perfil():
    """Exibe o Perfil do Utilizador (Estatísticas e Dados)."""
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    user = db.session.get(User, session['user_id']) # Uso a forma atualizada do SQLAlchemy
    return render_template('perfil.html', user=user)

@app.route('/logout')
def logout():
    """Termina a sessão do jogador e limpa os cookies."""
    session.clear()
    flash('Sessão terminada.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    """Rota protegida: Painel principal de gestão do teu jogo."""
    if 'user_id' not in session:
        flash('Precisas de iniciar sessão para jogar.', 'warning')
        return redirect(url_for('login'))
        
    user = db.session.get(User, session['user_id'])
    return render_template('dashboard.html', user=user)

@app.route('/colher', methods=['POST'])
def colher_recurso():
    """Colhe madeira ou telhas quando o utilizador clica no botão."""
    # Verifica se o jogador está com a sessão ativa (Lab 8)
    if 'user_id' not in session:
        flash('Precisas de iniciar sessão primeiro.', 'warning')
        return redirect(url_for('login'))
        
    # 1. Procura o jogador atual na Base de Dados
    user = db.session.get(User, session['user_id'])
    recurso = request.args.get('recurso')
    wants_json = request.accept_mimetypes.accept_json or request.is_json
    recursos_validos = {'madeira', 'telhas', 'comida', 'joias'}

    if recurso not in recursos_validos:
        # Return JSON for fetch requests or redirect for normal requests
        if wants_json:
            return jsonify({'success': False, 'message': 'Recurso inválido.'}), 400
        flash('Recurso inválido.', 'danger')
        return redirect(url_for('dashboard'))
    
    # 2. Incrementa o recurso escolhido.
    quantidade = 2 if recurso == 'joias' else 5
    setattr(user, recurso, getattr(user, recurso) + quantidade)
        
    # 3. Guarda a alteração no jogo.db teste
    db.session.commit()
    
    # 4. For normal requests, flash a message; for fetch requests, return JSON
    if not wants_json:
        flash(f'+{quantidade} {recurso.capitalize()}!', 'success')

    # If this was a fetch request, return JSON with the new value
    if wants_json:
        return jsonify({'success': True, 'recurso': recurso, 'amount': quantidade, 'new_value': getattr(user, recurso)})

    # 5. Atualiza a página do dashboard com o novo valor
    return redirect(url_for('dashboard'))


def construir_edificio_por_tipo(tipo):
    if 'user_id' not in session:
        flash('Precisas de iniciar sessão primeiro.', 'warning')
        return redirect(url_for('login'))

    user = db.session.get(User, session['user_id'])
    info = EDIFICIOS_INFO.get(tipo)

    if info is None:
        flash('Edifício inválido.', 'danger')
        return redirect(url_for('dashboard'))

    for recurso_necessario, quantidade_necessaria in info['custo'].items():
        if getattr(user, recurso_necessario) < quantidade_necessaria:
            flash(f'Não tens recursos suficientes para construir {tipo.capitalize()}.', 'warning')
            return redirect(url_for('dashboard'))

    for recurso_necessario, quantidade_necessaria in info['custo'].items():
        setattr(user, recurso_necessario, getattr(user, recurso_necessario) - quantidade_necessaria)

    setattr(user, info['coluna'], getattr(user, info['coluna']) + 1)

    if tipo == 'castelo':
        user.soldados += 5
        flash('O teu novo Castelo gerou 5 Soldados para o teu exército!', 'info')

    db.session.commit()

    flash(f'{tipo.capitalize()} construído(a) com sucesso!', 'success')
    return redirect(url_for('dashboard'))


@app.route('/construir_edificio', methods=['POST'])
def construir_edificio():
    tipo = request.args.get('tipo')
    return construir_edificio_por_tipo(tipo)


@app.route('/construir', methods=['POST'])
def construir():
    return construir_edificio_por_tipo('casa')


@app.route('/recrutar_soldados', methods=['POST'])
def recrutar_soldados():
    if 'user_id' not in session:
        flash('Precisas de iniciar sessão primeiro.', 'warning')
        return redirect(url_for('login'))

    user = db.session.get(User, session['user_id'])

    for recurso_necessario, quantidade_necessaria in RECRUTAR_SOLDADOS_CUSTO.items():
        if getattr(user, recurso_necessario) < quantidade_necessaria:
            flash('Não tens recursos suficientes para recrutar soldados.', 'warning')
            return redirect(url_for('dashboard'))

    for recurso_necessario, quantidade_necessaria in RECRUTAR_SOLDADOS_CUSTO.items():
        setattr(user, recurso_necessario, getattr(user, recurso_necessario) - quantidade_necessaria)

    user.soldados += RECRUTAR_SOLDADOS_GANHO
    db.session.commit()

    flash(f'+{RECRUTAR_SOLDADOS_GANHO} Soldados recrutados com sucesso!', 'success')
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    def find_available_port(start_port, host="127.0.0.1", max_tries=20):
        for port in range(start_port, start_port + max_tries):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                if sock.connect_ex((host, port)) != 0:
                    return port
        raise RuntimeError(f"Nenhuma porta livre encontrada a partir de {start_port}.")

    desired_port = int(os.getenv("PORT", app.config.get("PORT", 5000)))
    port = find_available_port(desired_port)

    if port != desired_port:
        print(f"Porta {desired_port} em uso; a iniciar na porta {port}.")

    app.run(host="0.0.0.0", port=port)
