from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)

  
    madeira = db.Column(db.Integer, default=5)
    telhas = db.Column(db.Integer, default=5)
    casas = db.Column(db.Integer, default=0)

    def set_password(self, password):
        """Guarda a palavra-passe usando hashing seguro (Lab 8)."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica se a password introduzida bate certo com o hash."""
        return check_password_hash(self.password_hash, password)