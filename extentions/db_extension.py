from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
# from sqlalchemy.ext.declarative import declarative_base
import config.db_config as db_config

try:
    Engine = create_engine(f"{db_config.PROTOCOL}{db_config.DB_USER}:{db_config.DB_PASSWORD}@{db_config.DB_HOST}:{db_config.DB_PORT}/{db_config.DB_NAME}")
    Base = declarative_base()
    Session = sessionmaker(bind=Engine)

except sqlalchemy.exc.ProgrammingError as SQLError: 
    print(f'\nsql-error= {SQLError}')
    
except  Exception as e:
    print(f"\nglobal-error caught {e}")    