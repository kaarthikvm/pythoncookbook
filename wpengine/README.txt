Software Requirement
=====================
Python version = 2.7
Python inbuilt packages used = csv, requests, unittest, sys


Input CSV file location
=======================
data/input.csv


Code Execution Usage
=====================
1. Inside top level source directory give the  following command in shell
   
    python main.py data/input.csv <location of output file>

    Eg: 
    python main.py data/input.csv output.csv



Test Execution
===============
1. Inside top level source directory after extraction
   Set PYTHONPATH to locate source modules 
   
   Eg: 
   export PYTHONPATH=$PWD

2. change to "tests" directory
   Eg: cd tests 
3. Run test using following command
   python test_task.py

Software Distribution using setup.py
====================================
To create tar ball distribution,issue the following command
from top level directory

   python setup.py sdist
 

After execution, tar ball for distribution can be located
inside "dist" folder

