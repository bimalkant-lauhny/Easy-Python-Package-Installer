import sys
import os
import requests
import json
import sqlite3
from utilities.autocomplete import get_packages_all_with
from utilities.update_packages import update_db


def installPackages(command):
    packages = command.split()[1:]
    # install each package
    for package in packages:
        print("Installing package: {package}".format(package=package))
        os.system("pip install {package}".format(package=package))
    # update requirements.txt
    os.system("pip freeze > requirements.txt")

def removePackages(command):
    packages = command.split()[1:]
    # install each package
    for package in packages:
        print("Removing package: {package}".format(package=package))
        os.system("pip uninstall {package}".format(package=package))
    # update requirements.txt
    os.system("pip freeze > requirements.txt")

def exitInterp(command):
    print("Bye!")
    sys.exit(0)

def getDocLink(command):
    packages = command.split()[1:]
    print("Visit following links:")
    for package in packages:
        print("https://pypi.org/project/{package}".format(package=package))

def getInstalledPackages(command):
    os.system("pip list")

def showHelp(command):
    with open("helpdocs.txt", "r") as helpdocs:
        print(helpdocs.read())

def fullSearch(command):
    package = command.split()[1]
    package_list = get_packages_all_with(package)
    for package in package_list:
        print (package)
    print("\nPackages Found: {}".format(len(package_list)))

def refreshPackageNames(command):
    print("Updating package database ...")
    update_db()

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

