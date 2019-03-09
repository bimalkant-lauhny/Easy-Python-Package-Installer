import readline
import sqlite3

# commands = ["req", "request", "asd", "asdfg", "try", "trywith"]
def autocomplete_packages(text):
    # print("Text supplied: ", text)
    with sqlite3.connect("packages.db") as conn:
        cur = conn.cursor()
        query = "SELECT * FROM packages WHERE name LIKE '%{text}%'".format(text=text)
        print("query: ", query)
        cur.execute(query)
        results = cur.fetchall()
        print("Fetch values: ", results)
        return results

def completer(text, state):
    auto_packages = autocomplete_packages(text)
    options = [i for i in auto_packages if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

while True:
    a = input("> ")
    print ("You entered", a)

