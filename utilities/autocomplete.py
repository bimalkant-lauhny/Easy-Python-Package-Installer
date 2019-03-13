import sqlite3

def get_packages_starting_with(text):
    with sqlite3.connect("db/packages.db") as conn:
        cur = conn.cursor()
        query = "SELECT name FROM packages WHERE name LIKE '{text}%' LIMIT 15".format(text=text)
        cur.execute(query)
        
        results = [x[0] for x in cur.fetchall()]
        return results

def get_packages_all_with(text):
    with sqlite3.connect("db/packages.db") as conn:
        cur = conn.cursor()
        query = "SELECT name FROM packages WHERE name LIKE '%{text}%'".format(text=text)
        cur.execute(query)
        
        results = [x[0] for x in cur.fetchall()]
        return results

