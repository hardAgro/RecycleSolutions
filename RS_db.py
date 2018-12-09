import time
import sqlite3
import requests
from sqlite3 import Error
from bs4 import BeautifulSoup

db_file = "C:\\sqlite\db\install_db_test_2.db"

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def insert_into_db(conn, table_name, a40_valor, a40_resultado, a41_valor, a41_resultado, a42_valor, a42_resultado, a43_valor, a43_resultado):
    sql = ''' INSERT INTO {0} (a40, a40_result, a41, a41_result, a42, a42_result, a43, a43_result, readtime) VALUES({1}, "{2}", {3}, "{4}", {5}, "{6}", {7}, "{8}", datetime('now')) '''.format(table_name, a40_valor, a40_resultado, a41_valor, a41_resultado, a42_valor, a42_resultado, a43_valor, a43_resultado)
    print(sql)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()

def get_data_and_save():
    #     soup = BeautifulSoup(arduino_page,'html.parser')
    #     string_arduino = soup.body.get_text()

    arduino_page = "http://192.168.1.100"

    page_response = requests.get(arduino_page, timeout=5)
    arduino_page_content = BeautifulSoup(page_response.content, "html.parser")
    string_arduino = arduino_page_content.body.get_text()

    # Extract Valor A40
    valor_a40_string = string_arduino.split("Porta A40 - Valor: ",1)[1]
    valor_a40_string = valor_a40_string[:valor_a40_string.find("\n")]
    valor_a40 = float(valor_a40_string)
    
    # Extract Valor A41
    valor_a41_string = string_arduino.split("Porta A41 - Valor: ",1)[1]
    valor_a41_string = valor_a41_string[:valor_a41_string.find("\n")]
    valor_a41 = float(valor_a41_string)

    # Extract Valor A42
    valor_a42_string = string_arduino.split("Porta A42 - Valor: ",1)[1]
    valor_a42_string = valor_a42_string[:valor_a42_string.find("\n")]
    valor_a42 = float(valor_a42_string)

    # Extract Valor A43
    valor_a43_string = string_arduino.split("Porta A43 - Valor: ",1)[1]
    valor_a43_string = valor_a43_string[:valor_a43_string.find("\n")]
    valor_a43 = float(valor_a43_string)

    # add below the conditions to the scale
    
    db_conn = create_connection(db_file)

    insert_into_db(db_conn, "leitura_arduino", valor_a40, "emanuel", valor_a41, "resultado_a41", valor_a42, "resultado_a42", valor_a43, "resultado_a43")

x=0
# Set to True instead of 3 to continuously run the reads
while x < 15:
    get_data_and_save()
    print("Saved in DB")
    x = x+1
    time.sleep(5) # change time (in seconds) to demonstrate app