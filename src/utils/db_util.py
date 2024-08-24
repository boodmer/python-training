from psycopg2.extensions import connection
from .db import get_db_conn, release_db_conn


def execute_query(query: str, params: tuple = ()) -> list:
    """Execute a read query and return results.

    Args:
        query (str): The SQL query to execute.
        params (tuple, optional): Parameters to pass to the query.

    Returns:
        list: Query results as a list of tuples.
    """
    conn: connection = get_db_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            results = cursor.fetchall()
            return results
    finally:
        release_db_conn(conn)


def execute_command(command: str, params: tuple = ()) -> None:
    """Execute a write command (e.g., INSERT, UPDATE) and commit changes.

    Args:
        command (str): The SQL command to execute.
        params (tuple, optional): Parameters to pass to the command.
    """
    conn: connection = get_db_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(command, params)
            conn.commit()
    finally:
        release_db_conn(conn)
