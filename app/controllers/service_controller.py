from app.extensions import db
from app.models.service import Service
from app.schemas.service_schema import ServiceSchema
from app.utils.response import success_response

service_schema = ServiceSchema()
service_schema = ServiceSchema(many=True)


def listar_servico():
    servicos = Service.query.all()
    return success_response(service_schema.dump(servicos)


def criar_servico(data):
    dados_validados = service_schema.load(data)

    novo_servico = Service(**dados_validados)

    db.session.add(servico)
    db.session.commit()

    return success_response(service_schema.dump(servico), 201)


def atualservico(id, datservico = Service.query.get_or_404(id)

    dados_validados = service_schema.load(data, partial=True)

    for campo, valor in dados_validados.items():
        setservico, campo, valor)

    db.session.commit()

    return success_response(service_schema.servico))


def delservico(iservico = Service.query.get_or_404(id))

    db.session.delete(servico)
    db.session.commit()

    return "", 204
