from models.schools import School
import uuid
class SchoolService(School):
    
    def __init__(self,session):
        self.session = session
    
    def create_school(self,data):
        try:
            print(f'data-- {data}')
            id = str(uuid.uuid4())
            name = data.get('name')
            email = data.get('email')
            total_room = data.get('total_room')
            province = data.get('province')
            
            school = School(id=id,name=name, email=email, total_room=total_room, province=province)
            
            self.session.add(school)
            self.session.commit()

            return {
                "name": school.name,
                "email": school.email,
                "total_room": school.total_room,
                "province": school.province
            }
        except Exception as e:
            self.session.rollback()
            print(f'error {e}')
            raise Exception(f'from <school_service> Error= {e} ')
    
    def get_schools(self):
        try:
            fetched = self.session.query(School).all()
            return [
                        { 
                            "id":school.id,
                            "name":school.name,
                            "email": school.email,
                            "total_room": school.total_room,
                            "province": school.province
                        } for school in  fetched
                ]
        except Exception as e :
            self.session.rollback()
            print(f'error {e}')
            raise Exception(f'from <school_service> Error= {e} ')
    
    
    def get_school(self,id):
        try:
            school= self.session.query(School).filter(School.id==id).first()    
            print(f'schooll {school}')
            return {
                "id": school.id,
                "name": school.name,
                "email": school.email,
                "total_room": school.total_room,
                "province": school.province
            }
        except Exception as e:
            self.session.rollback()
            print(f'from <school_service> Error= {e} ')
            # raise Exception(f'from <school_service> Error= {e} ')
    def school_exist(self,id):
        return  self.get_school(id) is not None
    
    def update_school(self,id,fields):
        try:
            to_update = self.get_school(id)
            if fields and to_update:
                for key,value in fields.items():
                    print(f'to_update --{key} {value} {to_update}')
                    to_update[key] = value
                    # setattr(to_update,key,value)
                self.session.commit()
                print(f'toupdate--{to_update}')
                return to_update
            return None
        except Exception as e : 
            self.session.rollback()
            print(f'error {e}')
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