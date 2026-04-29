from marshmallow import fields, validate

from app.extensions import ma
from app.models.services import Services


class ServicesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Services

    id = ma.auto_field(dump_only=True)
    nome = ma.auto_field(required=True)
    descricao = ma.auto_field(required=True, validate=validate.Length(min=1, max=256))
    ordens = fields.Nested("ServiceOrderSchema", only=("id", "descricao") )
    preco_base = fields.String(
        required=True,
        load_only=True,
        validate=validate.Length(min=5, max=7),
    )