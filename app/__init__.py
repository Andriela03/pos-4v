from flask import Flask
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound
from .config import Config
from .extensions import db, ma, migrate
from .routes.service import services_bp
from .routes.providers import providers_bp


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    from .models import service  # noqa: F401

    app.register_blueprint(providers_bp, url_prefix="/orders")
    app.register_blueprint(services_bp, url_prefix="/services")

    @app.errorhandler(ValidationError)
    def handle_validation_error(err):
        return {"success": False, "errors": {"nome": ["Campo obrigatório"]}}, 400

    @app.errorhandler(NotFound)
    def handle_not_found(err):
        return {"success": False, "message": "Recurso nao encontrado"}, 404

    @app.errorhandler(404)
    def handle_404(err):
        return {"success": False, "message": "Rota nao encontrada"}, 404

    return app
