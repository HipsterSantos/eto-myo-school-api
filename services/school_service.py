from models.schools import School
class SchoolService(School):
    
    def __init__(self,session):
        self.session = session
    
    def get_schools(self):
        return self.session.query(School).all()
    
    def get_school(self,id):
        school= self.session.query(School).filter(School.id==id).first()    
        return school
    
    def update_school(self,id,fields):
        to_update = self.get_school(id)
        if fields and to_update:
            for key,value in fields.items():
                setattr(to_update,key,value)
                self.session.commit()
            return to_update
        return []
    
    def delete_school(self, id):
        school = self.session.query(School).filter(School.id == id).first()
        if school:
            self.session.delete(school)
            self.session.commit()
            return True
        return False

    def soft_delete_school(self, id):
        school = self.session.query(School).filter(School.id == id).first()
        if school:
            school.soft_deleted = True
            self.session.commit()
            return True
        return False
        