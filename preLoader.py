from tfl_backend import get_pythons

Current_default_env = 'None'
Current_default_env_dir = 'None'


def check_installed_Python():
    pyvers = get_pythons()
    if pyvers[0]:
        if type(pyvers[1]) == type([]) and not len(pyvers[1]):
            return 0
        else:
            return 1















