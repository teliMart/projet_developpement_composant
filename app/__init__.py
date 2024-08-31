from flask import Flask, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_swagger_ui import get_swaggerui_blueprint


db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    
    app = Flask(__name__)
   
    # Configurer le Swagger UI
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'  # chemin vers votre fichier swagger.json
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={  # configuration supplémentaire
            'app_name': "API Hotel"
        }
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
      # Servir le fichier swagger.json
    @app.route('/static/swagger.json')
    def swagger_json():
        return send_from_directory(directory='static', path='swagger.json')
    
    app.config.from_object('config.Config')
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

    return app
