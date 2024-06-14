from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .controllers.image_controller import image_controller
    app.register_blueprint(image_controller)
    
    return app
