from marshmallow import fields

from app.extensions import ma
from app.models.service import Providers


class ProvidersSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Providers

    id = ma.auto_field(dump_only=True)
    descricao = ma.auto_field(required=True)
    status = ma.auto_field(required=True)   
    service_id = fields.Integer(required=True)