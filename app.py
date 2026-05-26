import os
import secrets
import socket

import flask
import models
import sqlalchemy

app = flask.Flask(__name__)
app.config.from_object("settings") 
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or app.config.get('SECRET_KEY') or secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

models.db.init_app(app)

with app.app_context():
    models.db.create_all()

    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        existing_columns = {
            row[1]
            for row in models.db.session.execute(sqlalchemy.text("PRAGMA table_info('user')"))
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
                models.db.session.execute(sqlalchemy.text(f"ALTER TABLE user ADD COLUMN {column_sql}"))
        models.db.session.commit()


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
    if 'user_id' in flask.session:
        return flask.redirect(flask.url_for('dashboard'))
    return flask.redirect(flask.url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if flask.request.method == 'POST':
        username = flask.request.form.get('username', '').strip()
        email = flask.request.form.get('email', '').strip()
        password = flask.request.form.get('password', '')
        dificuldade = flask.request.form.get('dificuldade', 'Normal')
        pergunta = flask.request.form.get('pergunta_seguranca', '')
        resposta = flask.request.form.get('resposta_seguranca', '').strip().lower() # Guardar em minúsculas
        avatar_escolhido = flask.request.form.get('avatar', 'default.png')
        
        if not username or not password or not email or not pergunta or not resposta:
            flask.flash('Todos os campos são obrigatórios!', 'danger')
            return flask.redirect(flask.url_for('register'))
            
        existing_user = models.User.query.filter((models.User.username==username) | (models.User.email==email)).first()
        if existing_user:
            flask.flash('Nome de utilizador ou email já em uso.', 'danger')
            return flask.redirect(flask.url_for('register'))
            
        # Criação do utilizador com os novos campos avançados teste 1 teste 2 teste 3 teste 4
        new_user = models.User(
            username=username, 
            email=email, 
            dificuldade=dificuldade,
            pergunta_seguranca=pergunta,
            resposta_seguranca=resposta,
            avatar=avatar_escolhido
        )
        new_user.set_password(password) # Usa o hashing reforçado
        
        models.db.session.add(new_user)
        models.db.session.commit()
        
        flask.flash('Conta criada com sucesso! Já podes entrar.', 'success')
        return flask.redirect(flask.url_for('login'))
        
    return flask.render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Valida as credenciais e inicia a sessão local do utilizador."""
    if flask.request.method == 'POST':
        username = flask.request.form.get('username', '').strip()
        password = flask.request.form.get('password', '')
        
        user = models.User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            flask.session['user_id'] = user.id
            flask.session['username'] = user.username
            flask.flash(f'Olá, {user.username}!', 'success')
            return flask.redirect(flask.url_for('dashboard'))
        else:
            flask.flash('Credenciais incorretas. Tenta novamente.', 'danger')
            
    return flask.render_template('login.html')


@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar_password():
    """Sistema de recuperação de conta baseado em pergunta de segurança."""
    if flask.request.method == 'POST':
        username = flask.request.form.get('username', '').strip()
        resposta = flask.request.form.get('resposta_seguranca', '').strip().lower()
        nova_password = flask.request.form.get('nova_password', '')
        
        user = models.User.query.filter_by(username=username).first()
        
        # Verifica se o utilizador existe e se a resposta bate certo
        if user and user.resposta_seguranca == resposta:
            user.set_password(nova_password)
            models.db.session.commit()
            flask.flash('A tua password foi reposta com sucesso! Podes fazer login.', 'success')
            return flask.redirect(flask.url_for('login'))
        else:
            flask.flash('Nome de utilizador ou resposta de segurança incorretos.', 'danger')
            
    return flask.render_template('recuperar.html')


@app.route('/perfil')
def perfil():
    """Exibe o Perfil do Utilizador (Estatísticas e Dados)."""
    if 'user_id' not in flask.session:
        return flask.redirect(flask.url_for('login'))
        
    user = models.db.session.get(models.User, flask.session['user_id']) # Uso a forma atualizada do SQLAlchemy
    return flask.render_template('perfil.html', user=user)

@app.route('/logout')
def logout():
    """Termina a sessão do jogador e limpa os cookies."""
    flask.session.clear()
    flask.flash('Sessão terminada.', 'info')
    return flask.redirect(flask.url_for('login'))

@app.route('/dashboard')
def dashboard():
    """Rota protegida: Painel principal de gestão do teu jogo."""
    if 'user_id' not in flask.session:
        flask.flash('Precisas de iniciar sessão para jogar.', 'warning')
        return flask.redirect(flask.url_for('login'))
        
    user = models.db.session.get(models.User, flask.session['user_id'])
    return flask.render_template('dashboard.html', user=user)

@app.route('/colher', methods=['POST'])
def colher_recurso():
    """Colhe madeira ou telhas quando o utilizador clica no botão."""
    # Verifica se o jogador está com a sessão ativa (Lab 8)
    if 'user_id' not in flask.session:
        flask.flash('Precisas de iniciar sessão primeiro.', 'warning')
        return flask.redirect(flask.url_for('login'))
        
    # 1. Procura o jogador atual na Base de Dados
    user = models.db.session.get(models.User, flask.session['user_id'])
    recurso = flask.request.args.get('recurso')
    wants_json = flask.request.accept_mimetypes.accept_json or flask.request.is_json
    recursos_validos = {'madeira', 'telhas', 'comida', 'joias'}

    if recurso not in recursos_validos:
        # Return JSON for fetch requests or redirect for normal requests
        if wants_json:
            return flask.jsonify({'success': False, 'message': 'Recurso inválido.'}), 400
        flask.flash('Recurso inválido.', 'danger')
        return flask.redirect(flask.url_for('dashboard'))
    
    # 2. Incrementa o recurso escolhido.
    quantidade = 2 if recurso == 'joias' else 5
    setattr(user, recurso, getattr(user, recurso) + quantidade)
        
    # 3. Guarda a alteração no jogo.db teste
    models.db.session.commit()
    
    # 4. For normal requests, flash a message; for fetch requests, return JSON
    if not wants_json:
        flask.flash(f'+{quantidade} {recurso.capitalize()}!', 'success')

    # If this was a fetch request, return JSON with the new value
    if wants_json:
        return flask.jsonify({'success': True, 'recurso': recurso, 'amount': quantidade, 'new_value': getattr(user, recurso)})

    # 5. Atualiza a página do dashboard com o novo valor
    return flask.redirect(flask.url_for('dashboard'))


def construir_edificio_por_tipo(tipo):
    if 'user_id' not in flask.session:
        flask.flash('Precisas de iniciar sessão primeiro.', 'warning')
        return flask.redirect(flask.url_for('login'))

    user = models.db.session.get(models.User, flask.session['user_id'])
    info = EDIFICIOS_INFO.get(tipo)

    if info is None:
        flask.flash('Edifício inválido.', 'danger')
        return flask.redirect(flask.url_for('dashboard'))

    for recurso_necessario, quantidade_necessaria in info['custo'].items():
        if getattr(user, recurso_necessario) < quantidade_necessaria:
            flask.flash(f'Não tens recursos suficientes para construir {tipo.capitalize()}.', 'warning')
            return flask.redirect(flask.url_for('dashboard'))

    for recurso_necessario, quantidade_necessaria in info['custo'].items():
        setattr(user, recurso_necessario, getattr(user, recurso_necessario) - quantidade_necessaria)

    setattr(user, info['coluna'], getattr(user, info['coluna']) + 1)

    if tipo == 'castelo':
        user.soldados += 5
        flask.flash('O teu novo Castelo gerou 5 Soldados para o teu exército!', 'info')

    models.db.session.commit()

    flask.flash(f'{tipo.capitalize()} construído(a) com sucesso!', 'success')
    return flask.redirect(flask.url_for('dashboard'))


@app.route('/construir_edificio', methods=['POST'])
def construir_edificio():
    tipo = flask.request.args.get('tipo')
    return construir_edificio_por_tipo(tipo)


@app.route('/construir', methods=['POST'])
def construir():
    return construir_edificio_por_tipo('casa')


@app.route('/recrutar_soldados', methods=['POST'])
def recrutar_soldados():
    if 'user_id' not in flask.session:
        flask.flash('Precisas de iniciar sessão primeiro.', 'warning')
        return flask.redirect(flask.url_for('login'))

    user = models.db.session.get(models.User, flask.session['user_id'])

    for recurso_necessario, quantidade_necessaria in RECRUTAR_SOLDADOS_CUSTO.items():
        if getattr(user, recurso_necessario) < quantidade_necessaria:
            flask.flash('Não tens recursos suficientes para recrutar soldados.', 'warning')
            return flask.redirect(flask.url_for('dashboard'))

    for recurso_necessario, quantidade_necessaria in RECRUTAR_SOLDADOS_CUSTO.items():
        setattr(user, recurso_necessario, getattr(user, recurso_necessario) - quantidade_necessaria)

    user.soldados += RECRUTAR_SOLDADOS_GANHO
    models.db.session.commit()

    flask.flash(f'+{RECRUTAR_SOLDADOS_GANHO} Soldados recrutados com sucesso!', 'success')
    return flask.redirect(flask.url_for('dashboard'))

# 1. Rota para mostrar a página HTML do Ranking
@app.route('/ranking')
def ranking_page():
    return flask.render_template('ranking.html')

# 2. Rota que fornece os dados em tempo real (A nossa API)
@app.route('/api/ranking')
def api_ranking():
    dados_ranking = models.User.get_leaderboard()
    return flask.jsonify(dados_ranking)


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
