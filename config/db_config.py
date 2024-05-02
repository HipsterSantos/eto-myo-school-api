import os

DB_NAME = os.getenv('DB_NAME') or 'postgres'
DB_PASSWORD = os.getenv('DB_PASSWORD') or '1234'
DB_HOST  = os.getenv('DB_HOST') or '0.0.0.0' 
DB_USER = os.environ['DB_USER']='postgres' or 'postgres'
DB_PORT = os.environ['DB_PORT']='5433' or '5433'
PROTOCOL = os.environ['DB_PROTOCOL']='postgresql://' or 'postgresql://'
