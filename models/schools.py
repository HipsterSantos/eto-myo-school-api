from sqlalchemy import create_engine,Column,Integer,String,UUID
from extentions.db_extension import Base
class School(Base):
    __tablename__ = "schools"    
    
    id = Column(UUID,primary_key=True)
    name = Column(String,unique=True,nullable=False)
    email = Column(String)
    province = Column(String(50))