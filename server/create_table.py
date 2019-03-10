import MySQLdb
import requests
from bs4 import BeautifulSoup
from config import HOST_NAME, USER_NAME, PASSWD, DB_NAME

def get_data():
    r = requests.get('https://pypi.org/simple/')
    data = BeautifulSoup(r.text)
    all_anchor_tags = data.find_all('a')

    packages_name = []
    for tag in all_anchor_tags:
        val = (str(tag.text),)
        packages_name.append(val)
    return packages_name

def main():
    with MySQLdb.MySQLdb.connect(host = HOST_NAME, user = USER_NAME, passwd = PASSWD, db = DB_NAME) as conn:
        f = open('time', 'r')
        content = f.read()
        if len(content) == 0 or (int) (time.time() - content) / (24 * 60 * 60) <= 24:
            cur = db.cursor()
            cur.execute('create table packages (name varchar(256) not null primary key')
            cur.execute('create table last_time_update (key int(1) primary key, time date not null')
            cur.executemany("INSERT into packages values(?)", get_data())


        f = open('time', 'w')
        f.write(str(time.time()))            
        

        
if __name__ == '__main__':
    main()