""" Paths to look for installed versions of python """

from os import getlogin,getcwd

pypath1=r'C:\Users\{}\AppData\Local\Programs\Python\Python37'.format(getlogin())
pypath2=r'C:\Users\{}\AppData\Local\Programs\Python37'.format(getlogin())
pypath3=r'C:\Users\{}\AppData\Local\Programs\Python37'.format(getlogin())
pypath4=r'C:\Program Files (x86)\Python37'
pypath5=r'C:\Program Files\Python37'
default_VE_NAME='TensorVEnvironment'

python_paths=[pypath1,pypath2,pypath3,pypath4,pypath5]

base_Directory=f'{getcwd()}\VEs'
default_VE=f'{getcwd()}\{default_VE_NAME}'

default_VE_user_defined=f'{getcwd()}'
emptyFileHandler=default_VE_NAME

installed_path=getcwd()
external_VE_baseDir=''

totalVEs = f'{installed_path}/Base/prefrencesData/database/Universal_01_DataPathStorage.db'
currentVE = f'{installed_path}/Base/prefrencesData/database/currentconfigVE.dat'
firstTExe = f'{installed_path}/Base/prefrencesData/database/001.dat'





















