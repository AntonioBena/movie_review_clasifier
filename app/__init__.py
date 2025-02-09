from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import review_blueprint
    app.register_blueprint(review_blueprint)
    return app