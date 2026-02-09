import psycopg2
from pgvector.psycopg2 import register_vector
from config import DB_CONFIG

def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    register_vector(conn)
    return conn
