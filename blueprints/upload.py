from flask import Blueprint,request,jsonify
import pandas as pd
from services.upload_service import UploadService
from services.school_service import SchoolService
from extentions.db_extension import Session

upload_bp = Blueprint('upload',__name__)
session =Session()

@upload_bp.post('/upload-file')
def upload_xlsx():
    try:
        if 'file' not in request.files or not request.files:
            return jsonify({
                "message":"Favor adiconar o arquivo",
                "status":400
            }), 400
            
        allowed_extensions = {'xlsx', 'xls'}
        if not request.files['file'].filename.lower().endswith(tuple(allowed_extensions)):
            return jsonify({'message': 'O arquivo deve estar no formato  Excel (xlsx, xls)'}), 400
        
        file = UploadService(request.files['file'])

        schools = file.from_excel_to_rows()
        result_set = []
        for school in schools:
            result_set.append( SchoolService(session).create_school(data={
                "name": school.name,
                "email": school.email,
                "total_room": school.total_room,
                "province": school.province
            })
            )        
        return jsonify({
            "message":" Todos os dados do excel importados com sucesso",
            "data": result_set
        }),200
    except Exception as e:
        print(f"an Error was found  Error =  {e} ")
        return jsonify({
            "message":" Erro ao importar dados do arquivo selecionado,<possivei emails ja existem no banco>"
        }),400