#!/usr/bin/env python

import os
import sys
import site
import json
import yaml
from pip._internal.utils.misc import get_installed_distributions


output = {}
# 1. version
pyver = ".".join(map(str, sys.version_info[:3]))
output.update({'current python version: ': pyver})

# 3. virtual environment
env = 'None'
if hasattr(sys, 'real_prefix'):
    env = os.popen('pyenv version').read()
output.update({'current virtualenv: ': env})

# 3.5 virtual environments and python versions lists
velsd = []
vels = os.popen('pyenv versions').read().split('\n')
for i in vels:
    if len(i):
        velsd.append(i)
output.update({'python / env-s list: ': velsd})

# 4. python executable location
output.update({'python executable: ': sys.executable})

# 5. pip location (each python version has its own version of pip)
piploc = os.popen('which pip').read()[:-1]
output.update({'current pip location: ': piploc})

# 6. PYTHONPATH
ppth = os.popen('echo $PYTHONPATH').read()[:-1]
output.update({'PYTHONPATH: ': ppth})

# 7. installed packages: name, version
plsd = {}
ls = get_installed_distributions()
for i in ls:
    t = str(i).split()
    plsd.update({t[0]: t[1]})
output.update({'packages list: ': plsd})

# 8. site-packages location
output.update({'side-packages location: ': site.getsitepackages()[0]})

jsonfilename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output.json')
ymlfilename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'output.yml')

with open(jsonfilename, 'w', encoding='utf-8') as logfile:
    try:
        json.dump(output, logfile, ensure_ascii=False, indent=4)
    except NameError:
        print('write error')

with open(ymlfilename, 'w', encoding='utf-8') as logfile:
    try:
        yaml.dump(output, logfile, indent=4)
    except NameError:
        print('write error')
