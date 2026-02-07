import psycopg

def get_db_connection():
    conn = psycopg.connect(
        dbname="research_db",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )
    return conn
