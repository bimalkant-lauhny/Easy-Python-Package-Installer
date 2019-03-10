import sqlite3
import requests
from bs4 import BeautifulSoup
from config import HOST_NAME, USER_NAME, PASSWD, DB_NAME
import time

def get_data():
    r = requests.get('https://pypi.org/simple/')
    data = BeautifulSoup(r.text, "lxml")
    all_anchor_tags = data.find_all('a')

    packages_name = []
    for tag in all_anchor_tags:
        val = (str(tag.text),)
        packages_name.append(val)
    
    return packages_name           

def update():
    with sqlite3.connect('packages.db') as conn:      
        f = open('time', 'r')
        content = f.read()

        if len(content) == 0 or  (time.time() - float(content)) / (24 * 60 * 60) > 24:
            print("Updating...")
        
            cur = conn.cursor()
            cur.execute('select name from packages')        
            old_packages = [x[0] for x in cur.fetchall()]
            new_packages = [x[0] for x in get_data()]

            diff = set(new_packages).difference(set(old_packages))
            diff = list(diff)

            if not diff:
                return

            diff = [(x,) for x in diff]
            cur.executemany("INSERT into packages values(?)", diff)