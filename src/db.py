import sqlite3
import random
import string

conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

def add_url(url):
    id = ""
    for _ in range(5):
        id += str(random.choice(string.printable))
    cursor.execute(f"INSERT INTO urls VALUES ('{id}', '{url}')")
    conn.commit()
    
def add_url_and_id(url, id):
    pass

def get_url(id):
    cursor.execute(f"SELECT * FROM urls WHERE id='{id}'")
    result = cursor.fetchone()
    return result[1]

def show_all():
    cursor.execute("SELECT * FROM urls")
    result = cursor.fetchall()
    print(result)
    
def close_connection():
    conn.close()