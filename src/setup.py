# from distutils.core import setup
# 
# setup(  name='mwhois',
#         version='0.1.10b',
#         author='Joel Cumberland',
#         description = "Multi Whois Client",
#         license='GPL',
#         py_modules=['mwhois', 'mthread', 'mgui']
#       )


import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "exclude":["wx"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "mwhois",
        version='0.1.10b',
        author='Joel Cumberland',
        description = "Multi Whois Client",
        license='GPL',
        options = {"build_exe": build_exe_options},
        executables = [Executable("mwhois.py", base=None)])