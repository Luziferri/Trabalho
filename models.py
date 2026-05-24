from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False) # Novo
    password_hash = db.Column(db.String(256), nullable=False)
    avatar = db.Column(db.String(100), default='default.png')
    
    dificuldade = db.Column(db.String(20), default='Normal')
    madeira = db.Column(db.Integer, nullable=False, default=0)
    telhas = db.Column(db.Integer, nullable=False, default=0)
    casas = db.Column(db.Integer, nullable=False, default=0)
    
    pergunta_seguranca = db.Column(db.String(100), nullable=False)
    resposta_seguranca = db.Column(db.String(100), nullable=False)

    def set_password(self, password):
        # 3. Medida Adicional de Segurança: HASHING REFORÇADO
        # Em vez do hash normal, forçamos o algoritmo pbkdf2 com 600.000 iterações!
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256:600000')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)