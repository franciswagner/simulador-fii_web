from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    conteudo_s_n = db.Column(db.Boolean, nullable=False)

    def __init__(self, nome, email, idade, conteudo_s_n):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.conteudo_s_n = conteudo_s_n
    
    def __repr__(self):
        return "<User %r>" % self.nome
