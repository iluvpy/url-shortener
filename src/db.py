import sqlite3
import random
import string

# XXX need a more safer way to access db.sqlite
def get_conn_and_c():
    conn = sqlite3.connect("db.sqlite")
    return conn, conn.cursor()

def random_id(c, len=5):
    id = ""
    for _ in range(5):
        id += random.choice(f"{string.ascii_letters}{string.digits}")

    res = get_url(id, c)
    if res == None:
        return id
    return random_id(c, len)


def add_url(url, conn, c) -> str:
    # find id that wasnt used yet
    id = random_id(c)
    
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


def get_all_urls(c):
    c.execute("SELECT * FROM urls")
    result = c.fetchall()
    return result

def show_all(c):
    print(get_all_urls(c))
    
