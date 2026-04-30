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
