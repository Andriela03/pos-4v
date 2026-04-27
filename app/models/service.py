from app.extensions import db

class Service(db.Model): 
    __tablename__ = "service"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    preco_base = db.Column(db.Integer, nullable=False)
    ordens = db.relationship(
        'ordem',
        backref='service',
        lazy=True,
        cascade='all, delete-orphan'
    )

class ServiceOrder (db.Model):
    __tablename__ = "serviceorder"
    id = db.Column(db.Column(db.Integer, primary_key=True))
    descricao = db.Column(db.String(225))
    status = db.Column(db.Bollean, nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)