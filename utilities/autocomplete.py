import sqlite3

def get_packages(text):
    with sqlite3.connect("db/packages.db") as conn:
        cur = conn.cursor()
        query = "SELECT name FROM packages WHERE name LIKE '{text}%' limit 10".format(text=text)
        cur.execute(query)
        
        results = [x[0] for x in cur.fetchall()]
        return results
