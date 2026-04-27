from flask import Blueprint, jsonify, request

from app.controllers.serviceorder_controller import criar_ordens, listar_ordens


orders_bp = Blueprint("orders", __name__)


@orders_bp.route("/", methods=["GET"])
def get_orders():
    response, status = listar_ordens()
    return jsonify(response), status


@orders_bp.route("/", methods=["POST"])
def post_orders():
    data = request.get_json()
    response, status = criar_ordens(data)
    return jsonify(response), status
