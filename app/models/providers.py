from app.extensions import db

providers_services = db.Table(
    "providers_services",
    db.Column("providers_id", db.Integer, db.ForeignKey("providers.id")),
    db.Column("service_id", db.Integer, db.ForeignKey("service.id"))
)