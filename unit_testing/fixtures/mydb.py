""" 
Author : Gurpreet Singh
Date : 19 Jan 2020
Purpose : To understand the working of fixture in test

###########
This is a dummy database class : Fake database  created for demonstaration purpose

>>> which has the same functionality as the real "Database module" has like oracle,mysql

>>> Functionality likes :
1.  Database object : "MyDB()" refers to MyDB class
2. connection Object : "connection()" refers to connection class
3. cursor object : "cursor()" refers to cursor class 
>> Cursor will have the abiltiy to execute your database query

"""


class MyDB:
    
    def __init__(self):
        self.connection = Connection()

    def connect(self,connection_string):
        return self.connection

class Connection:

    def __init__(self):
        self.cur = Cursor()

    def cursor(self):
        return self.cur 

    def close(self):
        pass       

class Cursor:

    def execute(self,query):
        if query == "select id from employee_db where name = John":
            return 123

        elif query == "select id from employee_db where name = Tom":
            return 789

        else:
            print("Some Error occured ")    
            return -1    

    
    def close(self):
        pass

""" 
###### Real Database #######

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print "Database version : %s " % data

# disconnect from server
db.close()

"""