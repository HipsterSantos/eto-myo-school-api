from flask import Flask
# from werkzeug.security import check_password_hash,generate_password_hash
from blueprints.school import school_bp
from blueprints.upload import upload_bp
from extentions.db_extension import Base,Engine
from services.province_service import ProvinceService
from flask_swagger_ui import get_swaggerui_blueprint
from flasgger import Swagger
def create_app():

    app = Flask(__name__)
    app.register_blueprint(school_bp)
    app.register_blueprint(upload_bp,url_prefix='/import')
    Base.metadata.create_all(bind=Engine)
    SWAGGER_URL = '/api/docs'
    API_URL = './swagger.json'
    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Your App Name"
        }
    )

    app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
    swagger = Swagger(app)

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    