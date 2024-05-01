import os

DB_NAME = os.environ['DB_NAME']='test_db' if not os.getenv('DB_NAME') else os.getenv('DB_NAME') or 'test_db'
DB_PASSWORD = os.environ['DB_PASSWORD']='1234' if not os.getenv('DB_PASSWORD') else os.getenv('DB_PASSWORD') or '1234'
DB_HOST  = os.environ['DB_HOST']='locahost' if not os.getenv('DB_HOST') else os.getenv('DB_HOST') or 'locahost'
DB_USER = os.environ['DB_USER']='postgres' if not os.getenv('DB_USER') else os.getenv('DB_USER') or 'postgres'