import pyodbc
def get_db_connection():
    conn = pyodbc.connect("Driver={MySQL ODBC 8.0 Unicode Driver};"
                          "Server=localhost;"
                          "Database=minmin;"
                          "UID=root;"
                          "PWD=minmin789;"
                          "charset=utf8mb4")
    return conn