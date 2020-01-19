""" 
Author : Gurpreet Singh
Date : 19 jan 2020
Purpose : Understand the working of fixtures

########
We are writing two units tests,
1. verify John's employee id
2. verify tom's employee id

"""
# import MySQLdb : database
from mydb import MyDB

def test_johns_id():
    # Open database connection
    # db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
    db = MyDB()
    conn = db.connect("server")

    # prepare a cursor object using cursor() method
    # cursor = db.cursor()
    cur = conn.cursor()

    # execute SQL query using execute() method.
    # cursor.execute("SELECT VERSION()")
    id = cur.execute("select id from employee_db where name = John")

    assert id == 123

def test_toms_id():
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()
    id = cur.execute("select id from employee_db where name = Tom")
    assert id == 789
        

""" 
Two issues in above code :

1. Code Repetition : if you have thousands test cases you have to write the same code again and again

2.Craating Database connection in every test case : which result in waste of some resources

######## How ways to fix those issues
1. setup and teardown methods (classic xunit style)
2. fixtures (recommended)

setup >>> initalize everything in begining you needs for your test case.

"""        
print("###### Setup - Tearndown ########")
conn  = None
cur = None

# setup at module level
def setup_module(module):
    global conn
    global cur
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()


# when all the test cases is done after then it excectued
def teardown_module(module):
    cur.close()
    conn.close()

def test_johns_id_1():
    id = cur.execute("select id from employee_db where name = John")
    assert id == 123

def test_toms_id_1():

    id = cur.execute("select id from employee_db where name = Tom")
    assert id == 789


""" 
fixtures : Fixtures leverage a concept of dependancy injection
doesn't need global varible

>> import pytest
>> @pytest.fixture()   # decorators
"""    
print("###### Fixture ########")

import pytest

# @pytest.fixture      # runs the cur function every time
@pytest.fixture(scope="module") # setup once at module level 
def cur1():
    print("Setting up ..")    # use cmd : pytest -v --capture=no
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    # return cur  
    yield curs          # it is used in order to close connection
    curs.close()
    conn.close()
    print("########  closing Database")

# This test is dependent on cur1
def test_johns_id_2(cur1):
    id = cur.execute("select id from employee_db where name = John")
    assert id == 123

def test_toms_id_2(cur1):

    id = cur.execute("select id from employee_db where name = Tom")
    assert id == 789



