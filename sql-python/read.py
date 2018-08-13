#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","vmk","jk","myinventory" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM Customer WHERE City = 'dublin'";
print sql;
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
       print "******************************************************"
       print "CID        %d" % row[0];
       print "FirstName  %s" % row[1];
       print "LastName   %s" % row[2];
       print "Address    %s" % row[3];
       print "City       %s" % row[4];
       print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
except Exception as e:
   print "Exception occured. Hence read failed";

# disconnect from server
db.close()

