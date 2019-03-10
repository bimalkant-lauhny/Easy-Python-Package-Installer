import sys
import os
import requests
import json
import sqlite3
from script import get_packages_name

server_url = "http://ec2-13-234-136-52.ap-south-1.compute.amazonaws.com:5000/"

def installPackages(command):
    packages = command.split()[1:]
    # install each package
    for package in packages:
        print("Installing package: {package}".format(package=package))
        os.system("pip install {package}".format(package=package))
    # update requirements.txt
    os.system("pip freeze > requirements.txt")

def exitInterp(command):
    print("Bye!")
    sys.exit(0)

def removePackages(command):
    packages = command.split()[1:]
    # install each package
    for package in packages:
        print("Removing package: {package}".format(package=package))
        os.system("pip uninstall {package}".format(package=package))
    # update requirements.txt
    os.system("pip freeze > requirements.txt")

def getDocLink(command):
    packages = command.split()[1:]
    print("Visit following links:")
    for package in packages:
        print("https://pypi.org/project/{package}".format(package=package))

def getInstalledPackages(command):
    os.system("pip list")

def showHelp(command):
    f = open("helpdocs.txt", "r")
    content = f.read()
    print(content)
    f.close()

def fullSearch(command):
    package = command.split()[1]
    print(package)
    options = {
        'q': package,
    }

    res = requests.get(server_url + 'search/adv?q={name}'.format(name=package))
    d = res.json()
    if d['code'] == 403:
        print (d['data'])
    else:
        for package in d['data']:
            print (package)

def getDataFromServer(package):
    res = requests.get(server_url + 'search?q={name}'.format(name=package))
    d = res.json()
    if d['code'] == 403:
        print (d['data'])
    else:
        return d['data']

def refreshPackageNames(command):
    with sqlite3.connect('db/packages.db') as conn:        
        print("Updating...")
        cur = conn.cursor()
        cur.execute('select name from packages')        
        old_packages = [x[0] for x in cur.fetchall()]
        new_packages = [x[0] for x in get_packages_name()]

        diff = set(new_packages).difference(set(old_packages))
        diff = list(diff)

        if not diff:
            return

        diff = [(x,) for x in diff]
        cur.executemany("INSERT into packages values(?)", diff)

def getOutdatedPackages(command):
    os.system("pip list --outdated")

def updatePackages(command):
    os.system("pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U")
    # update requirements.txt
    os.system("pip freeze > requirements.txt")

COMM_EXEC = {
    "install": installPackages,
    "remove": removePackages,
    "exit": exitInterp,
    "doc": getDocLink,
    "installed": getInstalledPackages,
    "help": showHelp,
    "adv": fullSearch,
    "refreshdb": refreshPackageNames,
    "update": updatePackages,
    "outdated": getOutdatedPackages,
}
