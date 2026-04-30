from app.extensions import db
from app.models.service import Service
from app.schemas.service_schema import ServiceSchema
from app.utils.response import success_response_service

service_schema = ServiceSchema()
services_schema = ServiceSchema(many=True)


def listar_servico():
    servicos = Service.query.all()
    return success_response_service(services_schema.dump(servicos))


def criar_servico(data):
    dados_validados = service_schema.load(data)

    novo_servico = Service(**dados_validados)

    db.session.add(novo_servico)
    db.session.commit()

    return success_response_service(service_schema.dump(novo_servico), 201)


def atualservico(id, data):
    servico = Service.query.get_or_404(id)

    dados_validados = service_schema.load(data, partial=True)

    for campo, valor in dados_validados.items():
        setattr(servico, campo, valor)

    db.session.commit()

    return success_response_service(service_schema.dump(servico))


def delservico(id):
    servico = Service.query.get_or_404(id)

    db.session.delete(servico)
    db.session.commit()

    return "", 204
