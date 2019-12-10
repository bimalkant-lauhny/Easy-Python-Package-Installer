import readline
from utilities import autocomplete
from utilities.commands import COMM_EXEC

def completer(text, state):
    if len(text) < 3:
        return None
    
    auto_packages = autocomplete.get_packages_starting_with(text)
    # auto_packages = getDataFromServer(text)
    if state < len(auto_packages):
        return auto_packages[state]
    else:
        return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)

if __name__ == '__main__':
    while True:
        interp_input = input("> ")
        command = interp_input.split()[0]
        if command not in COMM_EXEC:
            print("Unrecognized command!")
        else:
            COMM_EXEC[command](interp_input)

