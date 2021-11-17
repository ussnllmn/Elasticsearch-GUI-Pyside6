import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico']

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "Elasticsearch",
    version = "1.0.5",
    description = "Elasticsearch for Covid-19 Information Application",
    author = "Kridsanapong Buathongjun",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
