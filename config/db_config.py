import os

DB_NAME = os.getenv('DB_NAME') or 'postgres'
DB_PASSWORD = os.getenv('DB_PASSWORD') or '1234'
DB_HOST  = os.getenv('DB_HOST') or 'localhost'
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PORT = os.getenv('DB_PORT', '5433')
PROTOCOL = os.getenv('DB_PROTOCOL', 'postgresql://')