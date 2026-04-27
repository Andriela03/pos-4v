rom marshmallow import fields

from app.extensions import ma
from app.models.service import ServiceOrder


class ServiceOrderSchema(ma.SQLAlchemySchema):
    class Meta:
        model = ServiceOrder

    id = ma.auto_field(dump_only=True)
    descricao = ma.auto_field(required=True)
    status = ma.auto_field(required=True)   

    
