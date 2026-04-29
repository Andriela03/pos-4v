from app.extensions import db
from app.models.providers import ServiceOrder
from app.models.services import Services, Provider
from app.schemas.services_schema import ServicesOrder
from app.schemas.provider_schema import ProviderSchema
from app.utils.response import success_response


serviceorder_schema = ProviderSchema()
serviceorder_schema = ProviderSchema(many=True)


def listar_ordens():
    ordens = ServiceOrder.query.all()
    return success_response(serviceorder_schema.dump(ordens))


def listar_ordens_por_servico(service_id):
    service = Services.query.get_or_404(service_id)
    ordens = service.ordens
    return success_response(serviceorder_schema.dump(ordens))


def criar_ordens(data):
    dados_validados = serviceorder_schema.load(data)

    Services.query.get_or_404(dados_validados["service_id"])

    nova_ordem = ServiceOrder(**dados_validados)

    db.session.add(nova_ordem)
    db.session.commit()

    return success_response(serviceorder_schema.dump(nova_ordem), 201)
