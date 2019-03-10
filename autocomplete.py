import readline
import sqlite3
import os
from commands import COMM_EXEC, getDataFromServer

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
    # auto_packages = getDataFromServer(text)
    if state < len(auto_packages):
        return auto_packages[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

while True:
    interp_input = input("> ")
    command = interp_input.split()[0]
    if command not in COMM_EXEC:
        print("Unrecognized command!")
    else:
        COMM_EXEC[command](interp_input)

