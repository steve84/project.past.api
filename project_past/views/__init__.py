from .order import order_bp
from .user import user_bp


def init_app(app):
    app.register_blueprint(order_bp)
    app.register_blueprint(user_bp)