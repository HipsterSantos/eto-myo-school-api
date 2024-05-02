from flask import Blueprint,request,jsonify
import pandas as pd
from services.upload_service import UploadService
upload_bp = Blueprint('upload',__name__)

@upload_bp.post('/upload-file')
def upload_xlsx():
    if 'file' not in request.files or not request.files:
        return jsonify({
            "message":"Favor adiconar o arquivo",
            "status":403
        }), 403
    file = UploadService(request.files['file'])
    #take the file and extract the file usisng pandas
    result = file.from_excel_to_rows()
    print(f'result {result}')

    return jsonify({
        "message":"server reached successfully"
    })