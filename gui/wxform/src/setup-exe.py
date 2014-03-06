import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

#IMPORTANT: Make sure the target_name has the .exe at end of name .e.g example.exe
target_name = 'mwhois.exe'

if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "mwhois",
        version='1.0',
        author='jrosco',
        description = "Multi Whois Client",
        license='GPL',
        options = {"build_exe": build_exe_options},
        executables = [Executable("__init__.py", base=base, targetName=target_name)])