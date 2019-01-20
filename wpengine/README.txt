Software Requirement
=====================
Python version = 2.7
Python inbuilt packages used = csv, requests, unittest, sys


Input CSV file location
=======================
data/input.csv


Code Execution Usage
=====================
1. Unzip/Untar soruce file
2. Move to source directory after extraction
3. Inside source directory issue the following command in shell
   
    python main.py data/input.csv <location of output file>

    Eg: 
    python main.py data/input.csv output.csv



Test Execution
===============
1. Unzip/Untar source file
2. Move to source directory after extraction
3. Set PYTHONPATH to locate modules 
   
   Eg: 
   export PYTHONPATH=$PWD

3. change to "tests" directory
   Eg: cd tests 
4. Run test using following command
   python test_task.py


