import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

db_file = "C:\\sqlite\db\install_db_test_2.db" # Remeber to create the domain exactaly like this or make your own

def create_table(conn):
    sql = ''' 
        CREATE TABLE IF NOT EXISTS leitura_arduino (
         id integer PRIMARY KEY AUTOINCREMENT,
         a40 float NOT NULL,
         a40_result text,
         a41 float NOT NULL,
         a41_result text,
         a42 float NOT NULL,
         a42_result text,
         a43 float NOT NULL,
         a43_result text,
         readtime DATE
        )
    '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()

db_conn = create_connection(db_file)
create_table(db_conn)