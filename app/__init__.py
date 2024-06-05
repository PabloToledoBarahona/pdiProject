from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import main
    from .controllers.image_controller import image_controller

    app.register_blueprint(main)
    app.register_blueprint(image_controller, url_prefix='/image')

    return app
