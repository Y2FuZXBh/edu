### objectives

- Control Structures and Iteration
```
The candidate will be able to create and analyze simple control structures, including conditionals (if/else/elif) and for/while loops using Python.
```
```py
if True:
    print("this")
eif False:
    print("that")
else:
    print("none")
```
- Creation of Executables
```
The candidate will have a basic understanding of creating a Python executable for Windows clients with a focus on penetration testing. This includes an understanding of backdoor functionality, the conversion of a Python program to an executable file, and using Python to create an executable that will evade most modern anti-virus signatures.
```
```py
import os
import py2exe # https://github.com/py2exe/py2exe/blob/master/docs/py2exe.freeze.md
import cx_freeze # https://cx-freeze.readthedocs.io/en/stable/index.html
import briefcase # https://briefcase.readthedocs.io/en/latest/reference/index.html#reference

# PyInstaller
# https://pyinstaller.org/en/stable/usage.html#using-pyinstaller
os.system("pyinstaller myscript.py")

# Nuitka
# https://github.com/Nuitka/Nuitka#nuitka-user-manual
os.system("nuitka --help")
```
- Data Analysis with Python
```
The candidate will demonstrate the ability to use Python for various data analysis techniques including parsing binary data with the struct module, common file formats, log analysis and statistics with freq.py, counters and sets, long tail and short-tail analysis.
```
```py
import struct
from collections import Counter
import numpy as np

# freq.py
# https://github.com/MarkBaggett/freq
```
- Data Structures
```
The candidate will be able to create and manipulate variable types and data structures, including bytes, byte arrays, byte encoded unicode characters using UTF-8 and Latin-1, integers, Python 3 strings, sets and sequential data structures, including dictionaries, lists, and tuples.
```
```py
import struct

string = "1"
number = int(string)
fraction = float(number)

decimal = ord(string)

hexadecimal = hex(decimal)
binary = bin(decimal)[2:]
byte = struct.pack("B", decimal)
character = chr(decimal)

bytes()
bytearray()

str() | ""
int() | 0
float() | 0.1

set()
list() | []
dict() | {}
tuple() | ()
```
- Database Interaction
```
The candidate will understand how to create a Python program to query databases using SQL libraries.
```
```py
import sqlite3 # https://docs.python.org/3/library/sqlite3.html
import pymysql # https://pymysql.readthedocs.io/en/latest/
import psycopg2 # https://www.psycopg.org/docs/
```
- Exception Handling
```
The candidate will have a basic understanding of Python exception handling capabilities, and how to build these into a program.
```
- Functions, Classes and Objects
```
The candidate will be able to demonstrate an understanding of Python functions, classes, and object oriented programming.
```
- Network Interfaces
```
The candidate will be able to implement TCP and UDP network based communications using Pythons socket module.
```
- Packet Analysis with Python
```
The candidate will understand how to use extended functionality of Python and Scapy to create, read, analyze, and manipulate captured network traffic.
```
- Python Basics
```
The candidate will be able to implement the more fundamental elements of Python, including creating, debugging and executing a program, and user/file input and output.
```
- Regular Expressions
```
The candidate will have a basic understanding of regular expressions, and how to implement them in searches with Python.
```
- Website Interaction
```
The candidate will understand how to use Python as a "browser" to interact with URLs and websites, handle cookies, and manipulate or capture traffic.
```