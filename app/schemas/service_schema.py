from marshmallow import fields, validate

from app.extensions import ma
from app.models.service import Service


class ServiceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Service

    id = ma.auto_field(dump_only=True)
    nome = ma.auto_field(required=True)
    descricao = ma.auto_field(required=True, validate=validate.Length(min=1, max=256))
    ordens = fields.Nested("ProviderSchema", only=("id", "descricao"))
    preco_base = fields.String(
        required=True,
        load_only=True,
        validate=validate.Length(min=5, max=7),
    )