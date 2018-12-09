from flask import Flask, render_template
import sqlite3
from sqlite3 import Error
import pandas as pd

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

# def avg_diff(df_in):


def read_table(conn, table_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {0}".format(table_name))
    results = cur.fetchall()
    return results[-9:]

app = Flask(__name__)

@app.route('/')
def main():
    db_file = "C:\\sqlite\db\install_db_test_2.db"

    db_conn = create_connection(db_file)
    
    arduino_data= read_table(db_conn, "leitura_arduino")
    
    return  render_template("index.html", rows = arduino_data)

app.run(debug=True, host="0.0.0.0", port=8002)