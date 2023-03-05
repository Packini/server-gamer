from sql import conexion as sql_conn
def query_db(query, args=()):
    conn = sql_conn.get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, args)
    conn.commit()
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results