import os

DB_NAME = os.environ['DB_NAME']='postgres' if not os.getenv('DB_NAME') else os.getenv('DB_NAME') or 'postgres'
DB_PASSWORD = os.environ['DB_PASSWORD']='1234' if not os.getenv('DB_PASSWORD') else os.getenv('DB_PASSWORD') or '1234'
DB_HOST  = os.environ['DB_HOST']='0.0.0.0' if not os.getenv('DB_HOST') else os.getenv('DB_HOST') or '0.0.0.0'
DB_USER = os.environ['DB_USER']='postgres' if not os.getenv('DB_USER') else os.getenv('DB_USER') or 'postgres'
DB_PORT = os.environ['DB_PORT']='5433' if not os.getenv('DB_USER') else os.getenv('DB_PORT') or '5433'
PROTOCOL = os.environ['DB_PROTOCOL']='postgresql://' if not os.getenv('DB_PROTOCOL') else os.getenv('DB_PROTOCOL') or 'postgresql://'
