import sys
import os

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

COMM_EXEC = {
    "install": installPackages,
    "remove": removePackages,
    "exit": exitInterp,
    "doc": getDocLink,
}

