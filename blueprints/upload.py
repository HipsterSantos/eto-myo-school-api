from flask import Blueprint,request,jsonify
import pandas as pd
upload_bp = Blueprint('upload',__name__)

@upload_bp.post('/upload-file')
def upload_xlsx():
    if 'file' not in request.files or not request.files:
        return jsonify({
            "message":"Favor adiconar o arquivo",
            "status":403
        }), 403
    file = request.files['file']
    #take the file and extract the file usisng pandas
    excell = pd.read_excel(file)
    print(f'{excell}')
    return jsonify({
        "message":"server reached successfully"
    })