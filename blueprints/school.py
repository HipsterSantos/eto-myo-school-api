from flask import Blueprint,request,jsonify,current_app
from models.schools import School
from extentions.db_extension import Session
import uuid
from services.province_service import ProvinceService
from services.school_service import SchoolService
import os
import json
school_bp = Blueprint('school',__name__)

session = Session()
local_json_file =  os.path.join( os.path.dirname(__file__),'../static/province.json')
province_service = ProvinceService(file_path=local_json_file)
school_service = SchoolService(session)

@school_bp.get('/schools')
def  get_schools():
    try:
        page = request.args.get(key='page',default=0,type=int)    
        result = school_service.get_schools()
        print(f"result -- {result}")
        return jsonify({
            "message": "result fetched is ",
            "page": page,
            "data": result
        }),200
        
    except Exception as e : 
        return jsonify({
            "message": f"An error was caught Error={e}",
        }),403
        
@school_bp.get('/schools/<id>')
def get_school(id):
    try:
        result_set = school_service.get_school(id)
        if not result_set: raise Exception("ID invalido , favor passar um id valido")
        return jsonify({
            "message":"Sussceffully fetched the data",
            "data": result_set
        })
    except Exception as e : 
        print(f"An error was caught Error={e}")
        return jsonify({
            "message": "Id invalido",
        }),403
        
@school_bp.post('/schools/create')
def create_school():
    data = request.json
    current_province = province_service.get_random_province().get("nome")
    try:
        new_school = school_service.create_school({
            "name": data.get("name"),
            "email": data.get("email"),
            "total_room": data.get("total_room"),
            "province": current_province
            })

        return jsonify({
            "message":"succssfully created!",
            "data": {
                "name": new_school.name,
                "email": new_school.email,
                "total_room": new_school.total_room,
                # "province" : province_service.get_full_province(new_school.province) or new_school.province
            }   
        })
    except Exception as e : 
        print(f"An error was caught Error={e}")
        return jsonify({
            "message": "Falha ao criar a escola, favor verificar os dados passados"
        }),403
         
@school_bp.put('/schools/update/<id>')
def update_school(id):
    try:
        data = request.json
        to_update = school_service.update_school(id,data) 
        
        return jsonify({
            "messaage":f" value {to_update}"
        })
    except Exception as e : 
        print(f"An error was caught Error={e}")
        return jsonify({
            "message": "Erro ao actualizar os dados , favor verificar a entrada ",
        }),403
     

@school_bp.delete('/schools/delete/<id>')
def soft_delete_school(id):
    try:
        data = request.json
        to_delete = school_service.update_school(id,data) 
        return jsonify({
            "messaage":f" value {to_delete}"
        })
    except Exception as e : 
        print(f"An error was caught Error={e}") #internal log for devs
        return jsonify({
            "message": "Erro ao apagar esta escola , favor verificar os dados",
        }),403

@school_bp.delete('/schools/soft-delete/<id>')
def delete_school(id):
    try:
        data = request.json
        to_delete = school_service.update_school(id,data) 
    except Exception as e : 
        print(f"An error was caught Error={e}") #internal log for devs
        return jsonify({
            "message": "Erro ao apagar esta escola , favor verificar os dados",
        }),403
