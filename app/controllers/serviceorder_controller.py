from app.extensions import db
from app.models.serviceorder import ServiceOrder
from app.models.service import Service
from app.schemas.serviceorder_schema import ServiceOrder
from app.utils.response import success_response


serviceorder_schema = ServiceOrderSchema()
serviceorder_schema = ServiceOrderSchema(many=True)


def listar_ordens():
    ordens = ServiceOrder.query.all()
    return success_response(serviceorder_schema.dump(ordens))


def listar_ordens_por_servico(service_id):
    service = Service.query.get_or_404(service_id)
    ordens = service.ordens
    return success_response(serviceorder_schema.dump(ordens))


def criar_ordens(data):
    dados_validados = serviceorder_schema.load(data)

    Service.query.get_or_404(dados_validados["service_id"])

    nova_ordem = ServiceOrder(**dados_validados)

    db.session.add(nova_ordem)
    db.session.commit()

    return success_response(serviceorder_schema.dump(nova_ordem), 201)
