from flask import Flask
# from werkzeug.security import check_password_hash,generate_password_hash
from blueprints.school import school_bp
from blueprints.upload import upload_bp
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.schools import School, Base
app = Flask(__name__)

app.register_blueprint(school_bp)
app.register_blueprint(upload_bp,url_prefix='/import')

if __name__ == "__main__":
    
    app.run(debug=True)
    