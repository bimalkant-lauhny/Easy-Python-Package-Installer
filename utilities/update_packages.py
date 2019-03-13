import requests
from bs4 import BeautifulSoup
import sqlite3

PACKAGE_LIST_URL = "https://pypi.org/simple/"
def get_packages_name():
    response = requests.get(PACKAGE_LIST_URL)
    data = BeautifulSoup(response.text, "lxml")
    all_anchor_tags = data.find_all("a")

    packages_name = []
    for tag in all_anchor_tags:
        val = (str(tag.text),)
        packages_name.append(val)
    return packages_name

def update_db():
    with sqlite3.connect("db/packages.db") as conn:
        cur = conn.cursor()
        try:
            cur.execute("CREATE TABLE IF NOT EXISTS packages (name TEXT PRIMARY KEY)")
            cur.execute("SELECT name FROM packages")
 
            old_list = [x[0] for x in cur.fetchall()]
            new_list = [x[0] for x in get_packages_name()]

            new_packages = set(new_list).difference(set(old_list))
            new_packages = list(new_packages)
            if not new_packages:
                return
            new_packages = [(x,) for x in new_packages]
            cur.executemany("INSERT INTO packages VALUES(?)", new_packages)
        except Exception as e:
            print("Exception occurred:", e)

