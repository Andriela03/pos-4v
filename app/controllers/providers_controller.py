from app.extensions import db
from app.models.service import Service, Providers
from app.schemas.providers_schema import ProvidersSchema
from app.utils.response import success_response_service


provider_schema = ProvidersSchema()
providers_schema = ProvidersSchema(many=True)


def listar_ordens():
    ordens = Providers.query.all()
    return success_response_service(providers_schema.dump(ordens))


def listar_ordens_por_servico(service_id):
    service = Service.query.get_or_404(service_id)
    ordens = service.providers
    return success_response_service(providers_schema.dump(ordens))


def criar_ordens(data):
    dados_validados = provider_schema.load(data)

    Service.query.get_or_404(dados_validados["service_id"])

    nova_ordem = Providers(**dados_validados)

    db.session.add(nova_ordem)
    db.session.commit()

    return success_response_service(provider_schema.dump(nova_ordem), 201)
