from flask import Blueprint, jsonify, request

from app.controllers.providers_controller import listar_ordens_por_servico
from app.controllers.service_controller import (
    atualservico,
    criar_servico,
    delservico,
    listar_servico,
)


services_bp = Blueprint("services", __name__)


@services_bp.route("/", methods=["GET"])
def get_services():
    response, status = listar_servico()
    return jsonify(response), status


@services_bp.route("/", methods=["POST"])
def post_services():
    data = request.get_json(force=True)
    response, status = criar_servico(data)
    return jsonify(response), status


@services_bp.route("/<int:id>", methods=["PATCH"])
def patch_services(id):
    data = request.get_json(force=True)
    response, status = atualservico(id, data)
    return jsonify(response), status


@services_bp.route("/<int:id>", methods=["DELETE"])
def delservices(id):
    response, status = delservico(id)
    if status == 204:
        return "", 204
    return jsonify(response), status


@services_bp.route("/<int:service_id>/orders", methods=["GET"])
def get_service_ordens(service_id):
    response, status = listar_ordens_por_servico(service_id)
    return jsonify(response), status
