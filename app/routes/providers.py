from flask import Blueprint, jsonify, request

from app.controllers.providers_controller import criar_ordens, listar_ordens


providers_bp = Blueprint("providers", __name__)


@providers_bp.route("/", methods=["GET"])
def get_orders():
    response, status = listar_ordens()
    return jsonify(response), status

@providers_bp.route("/", methods=["POST"])
def post_orders():
    data = request.get_json()
    response, status = criar_ordens(data)
    return jsonify(response), status

@providers_bp.route("/<int:id>/services/<int:service_id>", methods=["POST"])
def vincular_servico(id, service_id):
    response, status = adicionar_servico_ao_provider(id, service_id)
    return jsonify(response), status

@providers_bp.route("/<int:id>/services", methods=["GET"])
def get_provider_services(id):
    response, status = listar_servicos_do_provider(id)
    return jsonify(response), status
