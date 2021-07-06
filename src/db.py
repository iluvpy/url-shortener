import sqlite3
import random
import string

def random_id(len=5):
    id = ""
    for _ in range(len):
        id += random.choice(string.printable) 
    return id

def add_url(url, conn, c) -> str:
    # find id that wasnt used yet
    id = random_id()
    
    c.execute(f"INSERT INTO urls VALUES ('{id}', '{url}')")
    conn.commit()
    return id
    
def add_url_and_id(url, id, conn, c):
    if get_url(id, c) == None:
        c.execute(f"INSERT INTO urls VALUES ('{id}', '{url}')")
        conn.commit()
        return "url created"
    return "url already exists"
    

def remove_url(id, conn, c):
    if get_url(id, c) != None:
        c.execute(f"DELETE FROM urls WHERE id='{id}'")
        conn.commit()
        return "url deleted"
    return "url does not exist or was already deleted"
    


def get_url(id, c):
    c.execute(f"SELECT * FROM urls WHERE id='{id}'")
    result = c.fetchone()
    if result != None:
        return result[-1]
    return None


def show_all(c):
    c.execute("SELECT * FROM urls")
    result = c.fetchall()
    print(result)
    
