from directory_manager import base_Directory, firstTExe,default_VE_NAME
from tfl_backend import universal_Path_database

with open(firstTExe) as file:
    try:
        terminator=int(file.read())
    except:
        terminator=0


""" This function checks that whether the software was previously was installed or not. """
""" Return redundatnt if yes or 0 if no """
def update_basedir_and_default_ve():
    global terminator
    if not terminator:
        universal_Path_database('add',default_VE_NAME,base_Directory)
        terminator=1
        writeTerminator(terminator)
        return 0
    else:
        return 'redundant'

def  writeTerminator(terminatorval):
    with open(firstTExe, 'w') as files:
        files.write(str(terminatorval))

# update_basedir_and_default_ve()