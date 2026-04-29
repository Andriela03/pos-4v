from marshmallow import fields

from app.extensions import ma
from app.models.services import Provider


class ProviderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Provider

    id = ma.auto_field(dump_only=True)
    descricao = ma.auto_field(required=True)
    status = ma.auto_field(required=True)   

    
