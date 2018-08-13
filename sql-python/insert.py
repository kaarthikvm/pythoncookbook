#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","vmk","jk","myinventory" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO Customer(FirstName, \
       LastName,Address,City) \
       VALUES ('%s', '%s', '%s', '%s')" % \
       ('bison','baby','addr7','limerick');
print sql;
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except Exception as e:
   print "Exception occured. Hence rolled back" + str(e);
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
