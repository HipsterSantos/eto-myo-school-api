from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Engine = create_engine("postgresql://postgres:1234@host/test_db")
Session = sessionmaker(bind=Engine)

Base = declarative_base()