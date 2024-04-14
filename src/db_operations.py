#db_operations
import psycopg2
import json
from datetime import datetime

# Database connection parameters
conn_params = {
    "database": "Final_Project",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5432"
}

def db_connect(func):
    """Decorator for database connection and cleanup."""
    def wrapper(*args, **kwargs):
        with psycopg2.connect(**conn_params) as conn:
            try:
                result = func(conn, *args, **kwargs)
                conn.commit()
                return result
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}")
    return wrapper

@db_connect
def execute_query(conn, query, args=None, fetch=False):
    """Execute a SQL query"""
    with conn.cursor() as cur:
        cur.execute(query, args)
        if fetch:
            return cur.fetchall()
        else:
            print("Operation successful.")