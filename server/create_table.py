import sqlite3
import requests
from bs4 import BeautifulSoup
from config import HOST_NAME, USER_NAME, PASSWD, DB_NAME
import time

def get_data():
    r = requests.get('https://pypi.org/simple/')
    data = BeautifulSoup(r.text)
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
        if len(content) == 0 or (int) (time.time() - content) / (24 * 60 * 60) <= 24:
            cur = conn.cursor()
            cur.execute('create table if not exists packages (name text primary key)')
            cur.executemany("INSERT into packages values(?)", get_data())


        f = open('time', 'w')
        f.write(str(time.time()))            
