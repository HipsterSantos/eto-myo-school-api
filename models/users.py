from sqlalchemy import Column,String,UUID
from extentions.db_extension import Base
from werkzeug.security import check_password_hash,generate_password_hash
class User(Base):
    __tablename__ = 'users'
    id = Column(UUID,primary_key=True)
    name = Column(String(10))
    email = Column(String(50),unique=True)
    hashed_password = Column(String(200),unique=True)
    token = Column(String)
    
    def set_password(password):
        pass
    def check_password(password):
        pass