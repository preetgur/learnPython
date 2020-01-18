"""
Author : Gurpreet Singh
Date : 17 Jan 2020
Purpose : Introduction to Testing framework in Python

#############
Python Testing Frameworks

1. unittest
2. nose
3. pytest  [best framework]

##########  
Install pytest : pip install pytest

########## Always save the name of test file with prefix "test_xyz.py" and the function should also be in same prefis " def test_fxn():"

############ How to Run Test file
cmd / gitbash : python -m pytest
cmd /gitbash : py.test
cmd / gitbash : py.tes -v

"""

def calc_total(a,b):
    return a+b

def calc_multiply(a,b):
    return a*b
