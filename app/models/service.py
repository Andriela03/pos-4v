from app.extensions import db
from app.models.providers import providers_services

class Service(db.Model): 
    __tablename__ = "service"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    preco_base = db.Column(db.Integer, nullable=False)

class Providers(db.Model):
    __tablename__ = "providers"
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(225))
    status = db.Column(db.String(50), nullable=False)
    services = db.relationship(
        "Service",
        secondary="providers_services",
        backref="providers"
)
