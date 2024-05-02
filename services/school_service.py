from models.schools import School
class SchoolService(School):
    def __init__(self,session):
        self.session = session
    def get_schools():
        return session.query(School).all()
    
    def get_school(id):
        school= session.query(School).filter(School.id==id).first()    
        return school
    
    def update_school(id,fields):
        to_udate = self.get_school(id)
        if fields and to_update:
            for ke,value in fields.items():
                seattr(to_update,key,value)
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
        