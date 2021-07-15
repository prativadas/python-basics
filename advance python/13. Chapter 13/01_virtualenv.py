# For MacOS/linux users: source myprojectenv/bin/activate
# For windows powershell users: .\myprojectenv\Scripts\activate.ps1
# https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

# install virtual env - pip install vitual env - isolated from other python env in the machine  
# then set a name for your env - virtualenv yourenvname - this makes a new virtual env
# activate the new env on terminal-  windows powershell users: .\myprojectenv\Scripts\activate.ps1  , here ps is powershell
# when env activated, it will be shown in terminal at the very begining of the line
# install all pacakges freshly on new virual env
# deactivate the new env - command: deactivate , then system interpreter is activated
#pip freeze will print all the packages in any env
# can save all the package names in requirement.txt file manually also or by command- pip freeze > requirement.txt

#pip install -r requirement.txt will install all packages into current activated env with one command

import flask # flask - 0.5.2              #you have to install all the package/modules before importing. pip install flask.
import pandas as pd
import pygame
