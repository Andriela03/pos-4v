from app.extensions import db

providers = db.Table(
    "providers_services",
    db.Column("providers_id", db.Integer, db.ForeingKey("providers.id")),
    db.Column("service_id", db.Integer, db.ForeignKey("services.id"))
)