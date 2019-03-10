import sqlite3
from config import HOST_NAME, USER_NAME, PASSWD, DB_NAME

def results(text):
    with sqlite3.connect('packages.db') as conn:
        cur = conn.cursor()
        query = "SELECT name FROM packages WHERE name LIKE '{text}%' limit 10".format(text=text)
        cur.execute(query)
        
        results = [x[0] for x in cur.fetchall()]
        return results