from datetime import datetime

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
    comida = db.Column(db.Integer, nullable=False, default=0)
    joias = db.Column(db.Integer, nullable=False, default=0)
    casas = db.Column(db.Integer, nullable=False, default=0)
    fazendas = db.Column(db.Integer, nullable=False, default=0)
    estradas = db.Column(db.Integer, nullable=False, default=0)
    castelos = db.Column(db.Integer, nullable=False, default=0)
    portos = db.Column(db.Integer, nullable=False, default=0)
    igrejas = db.Column(db.Integer, nullable=False, default=0)
    soldados = db.Column(db.Integer, nullable=False, default=0)
    cavalos = db.Column(db.Integer, nullable=False, default=0)
    last_resource_tick = db.Column(db.DateTime, nullable=True)
    
    pergunta_seguranca = db.Column(db.String(100), nullable=False)
    resposta_seguranca = db.Column(db.String(100), nullable=False)

    def get_resource_generation(self):
        return {
            'madeira': self.casas,
            'telhas': self.casas + (self.portos * 2),
            'comida': self.fazendas * 2,
            'joias': self.castelos + self.igrejas,
        }

    def set_password(self, password):
        # 3. Medida Adicional de Segurança: HASHING REFORÇADOaaaa
        # Em vez do hash normal, forçamos o algoritmo pbkdf2 com 600.000 iterações!
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256:600000')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_score(self):
        """Calcula a pontuação total com base no progresso guardado na BD."""
        return (
            self.madeira
            + self.telhas
            + self.comida
            + self.joias
            + (self.casas * 10)
            + (self.fazendas * 8)
            + (self.estradas * 5)
            + (self.castelos * 25)
            + (self.portos * 20)
            + (self.igrejas * 15)
            + (self.soldados * 3)
            + (self.cavalos * 2)
        )

    @classmethod
    def get_leaderboard(cls, limit=10):
        """Retorna os melhores jogadores ordenados pela pontuação calculada."""
        score_expression = (
            cls.madeira
            + cls.telhas
            + cls.comida
            + cls.joias
            + (cls.casas * 10)
            + (cls.fazendas * 8)
            + (cls.estradas * 5)
            + (cls.castelos * 25)
            + (cls.portos * 20)
            + (cls.igrejas * 15)
            + (cls.soldados * 3)
            + (cls.cavalos * 2)
        )

        jogadores = cls.query.order_by(score_expression.desc(), cls.username.asc()).limit(limit).all()
        return [{"username": jogador.username, "score": jogador.get_score()} for jogador in jogadores]