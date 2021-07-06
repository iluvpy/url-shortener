""" creates new database """

import sqlite3

conn = sqlite3.connect("db.sqlite")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE urls (
                id text,
                url text )""")
conn.commit()
conn.close()