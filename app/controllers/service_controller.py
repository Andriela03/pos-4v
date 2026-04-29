from app.extensions import db
from app.models.services import Services
from app.schemas.services_schema import ServicesSchema
from app.utils.response import success_response

services_schema = ServicesSchema()
services_schema = ServicesSchema(many=True)


def listar_servico():
    servicos = Services.query.all()
    return success_response(services_schema.dump(servicos))


def criar_servico(data):
    dados_validados = services_schema.load(data)

    novo_servico = Services(**dados_validados)

    db.session.add(novo_servico)
    db.session.commit()

    return success_response(services_schema.dump(novo_servico), 201)


def atualservico(id, data):
    servico = Services.query.get_or_404(id)

    dados_validados = services_schema.load(data, partial=True)

    for campo, valor in dados_validados.items():
        setattr(servico, campo, valor)

    db.session.commit()

    return success_response(services_schema.dump(servico))


def delservico(id):
    servico = Services.query.get_or_404(id)

    db.session.delete(servico)
    db.session.commit()

    return "", 204
