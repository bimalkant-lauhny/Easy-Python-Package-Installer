import MySQLdb
from config import HOST_NAME, USER_NAME, PASSWD, DB_NAME

def results(text):
    with MySQLdb.MySQLdb.connect(host = HOST_NAME, user = USER_NAME, passwd = PASSWD, db = DB_NAME) as conn:
        cur = conn.cursor()
        query = "SELECT name FROM packages WHERE name LIKE '{text}%' limit 10".format(text=text)
        cur.execute(query)
        
        results = [x[0] for x in cur.fetchall()]
        return results