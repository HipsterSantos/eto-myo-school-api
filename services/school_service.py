from models.schools import School
from .province_service import ProvinceService
import uuid
import os
import json

local_json_file =  os.path.join( os.path.dirname(__file__),'../static/province.json')
province_service = ProvinceService(file_path=local_json_file)

class SchoolService(School):
    
    def __init__(self,session):
        self.session = session
    
    def create_school(self,data):
        try:
            current_province = province_service.get_random_province().get("nome")
            print(f'data-- {current_province}')
            id = str(uuid.uuid4())
            name = data.get('name')
            email = data.get('email')
            total_room = data.get('total_room')
            province = current_province
            
            school = School(id=id,name=name, email=email, total_room=total_room, province=province)
            
            self.session.add(school)
            self.session.commit()

            return self.de_serialize(school)
        except Exception as e:
            self.session.rollback()
            print(f'error {e}')
            raise Exception(f'from <school_service> Error= {e} ')
    
    def get_schools(self,page=1,per_page=20):
        next_page = (page - 1) * per_page
        try:
            fetched = self.session.query(School).filter(School.soft_delete == False).offset(next_page).limit(per_page).all()
            return [
                    { 
                        **self.de_serialize(school)
                    } for school in  fetched
                ]
        except Exception as e :
            self.session.rollback()
            print(f'error {e}')
            raise Exception(f'from <school_service> Error= {e} ')
    
    def get_school(self,id):
        try:
            school= self.session.query(School).filter(School.id==id).first()    
            # print(f'schooll {school}')
            return school
        except Exception as e:
            self.session.rollback()
            print(f'from <school_service> Error= {e} ')
            # raise Exception(f'from <school_service> Error= {e} ')
    
    def school_exist(self,email):
        school= self.session.query(School).filter(School.email==email).first()    
        return  school is not None
    
    def de_serialize(self, school:School):
        print(f" full province detials: {province_service.get_full_province(school.name)}")
        return {
                "id": school.id,
                "name": school.name,
                "email": school.email,
                "total_room": school.total_room,
                "province": school.province
            }
    
    def update_school(self,id,fields):
        try:
            to_update = self.get_school(id)
            # to_update = School(**to_update)
            if fields and to_update:
                for key,value in fields.items():
                    setattr(to_update,key,value)
                self.session.commit()
                return self.de_serialize(to_update)
            return None
        except Exception as e : 
            self.session.rollback()
            print(f'error update{e}')
            raise Exception(f'from <school_service> Error= {e} ')
        
    def delete_school(self, id):
        try:
            school = self.get_school(id)
            if school:
                self.session.delete(school)
                self.session.commit()
                return True
            return False
        except Exception as e :
            self.session.rollback()
            print(f'error {e}')
            raise Exception(f'from <school_service> Error= {e} ')
        
    def soft_delete_school(self, id):
        try:
            school = self.get_school(id)
            if school:
                school.soft_deleted = True
                self.session.commit()
                return True
            return False
        except: 
            self.session.rollback()
            print(f'error {e}') # for dev log
            raise Exception(f'from <school_service> Error= {e} ')