import requests
from bs4 import BeautifulSoup
import sqlite3

def get_packages_name():
    r = requests.get('https://pypi.org/simple/')

    data = BeautifulSoup(r.text)

    all_anchor_tags = data.find_all('a')
    packages_name = []
    for tag in all_anchor_tags:
        packages_name.append((tag.text.encode('ascii', 'ignore'),))

def insert_into_db():
    with sqlite3.connect('packages.db') as conn:
        c = conn.cursor()
        try:
            # c.execute("CREATE TABLE if not exists packages (name text not null primary key)")
            # c.executemany("INSERT into packages values(?)", get_packages_name())
            for row in c.execute('select * from packages'):
                print row
        except Exception as e:
            print("Exception occurred", e)
            conn.rollback()

if __name__ == '__main__':
    insert_into_db()

