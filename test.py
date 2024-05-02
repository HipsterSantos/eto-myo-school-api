from sqlalchemy import create_engine,Column,Integer,String,UUID
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
# from sqlalchemy.ext.declarative import declarative_base
import config.db_config as db_config
import uuid
try:
    Engine = create_engine(f"{db_config.PROTOCOL}{db_config.DB_USER}:{db_config.DB_PASSWORD}@{db_config.DB_HOST}:{db_config.DB_PORT}/{db_config.DB_NAME}")
    Base = declarative_base()
    # Base.metadata.bind = Engine
    
    class Schools(Base):
        __tablename__ = "schools"    
        
        id = Column(UUID,primary_key=True)
        name = Column(String,unique=True,nullable=False)
        email = Column(String)
        province = Column(String(50))
    print('created ')
    school =[]
    Base.metadata.create_all(bind=Engine)
    Session = sessionmaker(bind=Engine)    
    session = Session()
    # for _ in range(20,30):
    #     school = Schools(
    #         id=str(uuid.uuid4()),  # Generate UUID for the primary key
    #         name=f'Dummy School {_}',
    #         email=f'dummy{_}@example.com',
    #         province='Dummy Province'
    #     )
    # session.add(school)

    # # Commit the changes to the database
    # session.commit()
    result = session.query(Schools).all()
    print(f"result {result}")
# except sqlalchemy.exc.ProgrammingError as SQLError: 
#     print(f'\nsql-error= {SQLError}')
except  Exception as e:
    print(f"\nerror caught {e}")    
    
    

    
    