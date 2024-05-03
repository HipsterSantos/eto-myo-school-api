from flask import Blueprint,request,jsonify,current_app
from models.schools import School
from extentions.db_extension import Session
import uuid
from services.province_service import ProvinceService
from services.school_service import SchoolService


school_bp = Blueprint('school',__name__)
session = Session()
school_service = SchoolService(session)

@school_bp.get('/schools')
def  get_schools():
    try:
        page = request.args.get(key='page',default=0,type=int)    
        result = school_service.get_schools()
        if not result:
            return jsonify({
            "message": "Nenhum dado foi adicionado ate ao momento",
            }),400    
        
        return jsonify({
            "message": "Escola carregado com sucesso",
            "page": page,
            "data": result
            }),200
        
    except Exception as e : 
        print(f"An error was caught Error={e}")
        return jsonify({
            "message": "Erro ao carregar os dados",
        }),403
        
@school_bp.get('/schools/<id>')
def get_school(id):
    try:
        result_set = school_service.get_school(id)
        if not result_set: 
            return jsonify({
                "message":"ID invalido , favor passar um id valido"
                }),400
            
        return jsonify({
            "message":"Sussceffully fetched the data",
            "data": school_service.de_serialize(result_set)
        })
    except Exception as e : 
        print(f"An error was caught Error={e}")
        return jsonify({
            "message": "Id invalido",
        }),403
        
@school_bp.post('/schools/create')
def create_school():
    data = request.json
    if school_service.school_exist(data.get("email")):
        return jsonify({
            "message":"Ja existe uma escola registrada com este email"
        }),400
        
    try:
        new_school = school_service.create_school({
            "name": data.get("name"),
            "email": data.get("email"),
            "total_room": data.get("total_room"),
            })

        return jsonify({
            "message":"succssfully created!",
            "data": new_school
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
        if not school_service.get_school(id):
            return jsonify({
            "message": "Nenhum dado foi adicionado com este ID",
            }),400 
             
        to_update = school_service.update_school(id,data) 
        return jsonify({
            "messaage": "Dado actualizado com sucesso",
            "data": to_update
        })
    except Exception as e : 
        print(f"An error was caught Error={e}")
        return jsonify({
            "message": "Erro ao actualizar os dados , favor verificar a entrada ",
        }),403
     
@school_bp.delete('/schools/delete/<id>')
def delete_school(id):
   
    try:
        exists = school_service.get_school(id)
        if not exists:
            return jsonify({
            "message": "Nenhum dado foi encontrado com este id",
            }),400  
            
        to_delete = school_service.delete_school(id) 
        
        return jsonify({
            "message": "Escola apagada com sucesso"
        }), 200
        
    except Exception as e : 
        print(f"An error was caught Error={e}") #internal log for devs
        return jsonify({
            "message": "Erro ao apagar esta escola , favor verificar os dados",
        }),403
        
@school_bp.delete('/schools/soft-delete/<id>')
def soft_delete_school(id):
    try:
        exists = school_service.get_school(id)
        if not exists:
            return jsonify({
            "message": "Nenhum dado foi encontrado com este id",
            }),400  
            
        to_delete = school_service.soft_delete_school(id) 
        
        return jsonify({
            "message": "Escola apagado com sucesso",
            "data": to_delete
        }), 200
        
    except Exception as e : 
        print(f"An error was caught Error={e}") #internal log for devs
        return jsonify({
            "message": "Erro ao apagar esta escola , favor verificar os dados",
        }),403


