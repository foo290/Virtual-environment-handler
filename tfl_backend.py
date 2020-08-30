import subprocess
import os
from directory_manager import python_paths, base_Directory, currentVE, totalVEs
from shutil import rmtree
import sqlite3
from pakages import messagebox



Current_default_env='None'; Current_default_env_dir = 'None'



thread_lock = 'open'

activeVE = ''

base_Directory = base_Directory

active_path = ''


def check_python_path():
    """ Returns 404 if python not found in any path """
    temp = []
    for paths in python_paths:
        if os.path.exists(paths):
            valid_path = f'{paths}\python.exe'
            if os.path.exists(valid_path):
                temp.append(1)
                return valid_path
            else:
                temp.append(0)
        else:
            temp.append(0)
    if not all(temp):
        return 404

thread_list=[]


def execute_VE(name, path, py_abs_path):
    try:
        py_Ver_found = check_python_path()
        if py_Ver_found != 404:
            if py_abs_path == py_Ver_found:

                subprocess.run(f'{py_abs_path} -m venv {path}\\{name} && exit()', shell=True, stdout=subprocess.PIPE)
                thread_list.append('success')
                return 'success'
            else:
                if os.path.exists(py_abs_path):

                    subprocess.run(f'{py_abs_path} -m venv {path}\\{name} && exit()', shell=True,
                                   stdout=subprocess.PIPE)
                    thread_list.append('success')
                    return 'success'
                else:
                    thread_list.append('customPythonPathWrong')
                    return 'customPythonPathWrong'
        else:
            thread_list.append('pythonNotFound')
            return 'pythonNotFound'
    except Exception as error:
        thread_list.append(error)
        return error


class Data_IO:
    def __init__(self):
        pass

    def writeDefaultVE(self, name):
        try:
            with open(currentVE, 'w') as file:
                file.write(f'{name}')
        except Exception as error:
            return -101, error

    def fetchDefaultVE(self):

        try:
            with open(currentVE, 'r') as file:
                raw_data = file.read()
                return raw_data
        except Exception as error:
            return -101, error


class Core_ops:
    def __init__(self):
        self.create_base_dir()
        pass

    def create_base_dir(self):
        if os.path.exists(base_Directory):
            pass
        else:
            os.mkdir(base_Directory)

    def open_jupyter(self, fun, type):
        global activeVE

        try:
            if activeVE != 'NotSpecified':
                if (activeVE != ''):

                    if Current_default_env_dir == base_Directory:
                        p2 = subprocess.Popen(['start', 'cmd', '/k',
                                               f'{f"{Current_default_env_dir}/{Current_default_env}/Scripts/activate.bat && cd {active_path}/{activeVE} && {type}"}'],
                                              shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                              stdout=subprocess.PIPE)
                        fun()
                        p2.wait(1)
                    else:

                        p2 = subprocess.Popen(['start', 'cmd', '/k',
                                               f'{f"{active_path}/Scripts/activate.bat && cd {active_path} && {type}"}'],
                                              shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE,
                                              stdout=subprocess.PIPE)
                        fun()
                        p2.wait(1)
                else:
                    return 0
            else:
                return 0
        except Exception as error:
            print(error)

    def create_new_virtual_environment(self, name, path, py_abs_path):
        """ Returns -201 if the VE already exist
            Return -101 if failed to create VE
        """
        try:
            if os.path.exists(f'{path}/{name}'):
                return -201
            else:
                if path == base_Directory and os.path.exists(path):
                    temp_ops = name.split(' ')
                    if len(temp_ops) > 1:
                        name = '_'.join(temp_ops)

                    response = execute_VE(name, path, py_abs_path)
                    # t1=Thread(target=execute_VE,args=[name, path, py_abs_path])
                    # t1.daemon=1
                    # t1.start()
                    # while 1:
                    #     try:
                    #         if thread_list[0]=='success':
                    #             response='success'
                    #             break
                    #         else:
                    #             response=thread_list[0]
                    #             break
                    #     except:
                    #         pass

                    if response == 'success':
                        universal_Path_database('add', name, path)
                        return 'success'
                    else:
                        return response
                else:
                    if os.path.exists(path):
                        temp_ops = name.split(' ')
                        if len(temp_ops) > 1:
                            name = '_'.join(temp_ops)

                        response = execute_VE(name, path, py_abs_path)
                        # t2 = Thread(target=execute_VE, args=[name, path, py_abs_path])
                        # t2.daemon = 1
                        # t2.start()
                        # while 1:
                        #     try:
                        #         if thread_list[0] == 'success':
                        #             response = 'success'
                        #             break
                        #         else:
                        #             response = thread_list[0]
                        #             break
                        #     except:
                        #         pass
                        if response == 'success':
                            universal_Path_database('add', name, path + name)
                            return 'success'
                        else:
                            return response
                    else:
                        return 'pathDontExist'
        except Exception as error:
            return -101, error

    def get_VE(self):
        """ Returns -1 if default VE is not available """

        VEs = os.walk(base_Directory).__next__()[1]

        VEs_2 = universal_Path_database('showall', '', '')

        final = [i for i in VEs_2 if i not in VEs]

        return 1, VEs + final

    def get_Packages(self, VEname, path, caller):
        if caller == 'internal':
            cmd = f'{base_Directory}/{VEname}/Lib/site-packages'
        else:
            cmd = f'{path}/Lib/site-packages'

        if os.path.exists(cmd):
            dirs = os.walk(cmd).__next__()
            if '__pycache__' in dirs[1]:
                dirs[1].remove('__pycache__')
            return dirs[1], dirs[2]
        else:
            return -1

    def deleteVENV(self, name):
        try:
            rmtree(f'{base_Directory}/{name}')
            return 1
        except Exception as error:
            return -1


def get_pythons():
    try:
        pythons = subprocess.run('py -0p', shell=True, stdout=subprocess.PIPE)
        hard_paths = pythons.stdout.decode('utf-8').strip().split('\n')

        python_dic={}
        for paths in hard_paths:
                python_dic[paths.strip().split('    ')[0]]=paths.strip().split('    ')[-1]
        if '(venv)' in python_dic.keys():
            python_dic.pop('(venv)')


        return 1, python_dic,

    except Exception as error:
        return 0, error


ver = get_pythons()


def validate_script(path, script_name):
    if os.path.exists(f'{path}/{script_name}'):
        version = path.split('/')[-1]
        return 1, version
    else:
        return 0,


def validate_VE_dir(path):
    if os.path.exists(f'{path}'):
        return 1
    return 0


def chk_valid_path_for_ve(path,name=''):
    if path==base_Directory:

        if os.path.exists(f'{path}/{name}/Scripts/python.exe'):
            return 1
        else:
            return 0
    else :
        if os.path.exists(f'{path}/Scripts/python.exe'):
            return 1
        else:
            return 0


def debug_func():
    import time
    time.sleep(2)
    return 'success'




class PrimaryExecution:
    def __init__(self):
        pass


    def get_previous_VE(self):
        with open(currentVE) as file:
            current = file.read()
        if os.path.exists(f'{base_Directory}/{current}'):
            if current !='' or current !=None:
                return 1,current,base_Directory
            else:
                return 101, #There was no active Env previously
        else:
            try:
                connection = sqlite3.connect(totalVEs)
            except:
                return -1, # Connection Error
            cur = connection.cursor()
            raw_data = cur.execute(f'select * from tab where name="{current}"')
            temp_raw = raw_data.fetchall()
            if len(temp_raw):
                _, currentVE_path = temp_raw[0]
                Dir_validation = validate_VE_dir(currentVE_path)
                if Dir_validation:
                    return 1,current,currentVE_path
                else:
                    return 102, # The directory of external VE is mmissing
            else:
                return 0, # The VE is invalid



def set_current():
    global Current_default_env_dir, Current_default_env,activeVE,active_path

    Chk_error = PrimaryExecution().get_previous_VE()
    if Chk_error[0] == 1:
        Current_default_env = Chk_error[1]
        Current_default_env_dir = Chk_error[2]

        activeVE=Current_default_env
        active_path=Current_default_env_dir
        return 1, Current_default_env, Current_default_env_dir

    elif Chk_error[0] == 101 or Chk_error[0] == -1 or not Chk_error[0]:
        messagebox.showerror('Missing Directories or Files', 'Something is not as what we expected!')
        return 0,

    elif Chk_error[0] == 102:
        messagebox.showerror('Missing Directories or Files', 'The previous VE Directory is no longer available.')
        return 0,
    else:
        return 0,

class Install_Pakages:
    def __init__(self):
        pass

    def install_pkgs_via_pip(self, name, dir, pkgname):
        target_dir = f'{dir}/{name}/Lib/site-packages'
        activate_cmd = f'{dir}/{name}/Scripts'
        install_cmd = f'pip install {pkgname}'

        p2 = subprocess.Popen(
            ['start', 'cmd', '/k', f'cd {activate_cmd} && activate.bat && cd {target_dir} && {install_cmd}'],
            shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        p2.wait(1)


def universal_Path_database(calltype, name, path,debug=None):
    temp_all_VE = []
    connection = sqlite3.connect(totalVEs)
    cur = connection.cursor()

    try:
        if calltype == "add":
            cur.execute('insert into tab values (?,?)', (name, path))
            connection.commit()
            return 1
        elif calltype == 'read':
            raw_file = cur.execute(f'select path from tab where name ="{name}"')
            data = raw_file.fetchall()[0][0]
            return data
        elif calltype == 'delete':
            cur.execute(f'delete from tab where name="{name}"')
            connection.commit()
            return 1
        elif calltype == 'showall':
            raw_file = cur.execute(f'select name from tab')
            data = raw_file.fetchall()

            for val in data:
                temp_all_VE.append(val[0])
            return temp_all_VE


        else:
            pass
    except Exception as error:
        return 0
    finally:
        connection.close()


def title_updater():
    return activeVE


# print(universal_Path_database('showall','',''))

set_current()
