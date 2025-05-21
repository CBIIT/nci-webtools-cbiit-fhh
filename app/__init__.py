from flask import Flask
from flask_oidc import OpenIDConnect

oidc = None

def create_app():
    global oidc
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    oidc = OpenIDConnect(app)

    # Register blueprints
    with app.app_context():
        from .routes import main
        from .api import api
        from .auth import auth

        app.register_blueprint(main)
        app.register_blueprint(api, url_prefix="/api")
        app.register_blueprint(auth, url_prefix="/auth")

    return app
