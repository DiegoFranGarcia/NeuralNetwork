import sqlite3


def get_bookmark_by_raw_sql_query(connection: sqlite3.Connection, query: str):
    cursor = connection.execute(query)
    row = cursor.fetchone()
    if row is None:
        return None
    columns = [description[0] for description in cursor.description]
    return dict(zip(columns, row))
