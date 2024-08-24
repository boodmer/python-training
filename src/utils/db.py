import psycopg2.pool
from psycopg2.extensions import connection
from os import getenv
from dotenv import load_dotenv

# preload env
load_dotenv()
# Database configuration
db_config = {
    'dbname': getenv('DB_NAME'),
    'user': getenv('DB_USER'),
    'password': getenv('DB_PASSWORD'),
    'host': getenv('DB_HOST'),  # or your database server IP
    'port': getenv('DB_PORT')  # Default PostgreSQL port
}

# Connection pool
connection_pool = psycopg2.pool.SimpleConnectionPool(1, 20, **db_config)


def get_db_conn() -> connection:
    """Get a database connection from the pool."""
    try:
        conn = connection_pool.getconn()
        return conn
    except Exception as e:
        print(f"Error getting database connection: {e}")
        raise


def release_db_conn(conn):
    """Release a database connection back to the pool."""
    try:
        connection_pool.putconn(conn)
    except Exception as e:
        print(f"Error releasing database connection: {e}")
        raise


def close_all_connections():
    """Close all connections in the pool."""
    connection_pool.closeall()
