from flask import Flask
# from werkzeug.security import check_password_hash,generate_password_hash
from blueprints.school import school_bp
from blueprints.upload import upload_bp
from extentions.db_extension import Base,Engine

def create_app():
    app = Flask(__name__)
    app.register_blueprint(school_bp)
    app.register_blueprint(upload_bp,url_prefix='/import')
    Base.metadata.create_all(bind=Engine)
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    