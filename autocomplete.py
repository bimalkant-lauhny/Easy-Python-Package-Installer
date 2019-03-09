import readline
import sqlite3
import os

def autocomplete_packages(text):
    with sqlite3.connect("packages.db") as conn:
        cur = conn.cursor()
        query = "SELECT name FROM packages WHERE name LIKE '{text}%' limit 10".format(text=text)
        cur.execute(query)
        
        results = [x[0] for x in cur.fetchall()]
        return results

def completer(text, state):
    if len(text) < 3:
        return None
    
    auto_packages = autocomplete_packages(text)
    if state < len(auto_packages):
        return auto_packages[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

while True:
    a = input("> ")
    if a == ".exit":
        print ("Bye!")
        break
    command = "pip install {package}".format(package=a)
    print("Installing {package} ...".format(package=a))
    os.system(command)