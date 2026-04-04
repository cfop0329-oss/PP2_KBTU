import psycopg2
from psycopg2._psycopg import connection

from config import DB_CONFIG


def get_connection() -> connection:
    return psycopg2.connect(
        host=DB_CONFIG["host"],
        dbname=DB_CONFIG["dbname"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        port=DB_CONFIG["port"]
    )