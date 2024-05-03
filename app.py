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
    try:
        app.register_blueprint(school_bp)
        app.register_blueprint(upload_bp,url_prefix='/import')
        Base.metadata.create_all(bind=Engine)
        SWAGGER_URL = '/api/docs'
        API_URL = '/static/swagger.json'
        swagger_ui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={
                'app_name': "School api"
            }
        )

        app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

        return app
    except Exception as e :
        print(f" An error occured {e}")
        return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    