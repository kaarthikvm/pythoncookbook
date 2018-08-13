#!/usr/bin/python

import MySQLdb

def basic_connection():
    # Open database connection
    db = MySQLdb.connect("localhost","vmk","jk","myinventory" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # execute SQL query using execute() method.
    cursor.execute("SELECT VERSION()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print "Database version : %s " % data

    # disconnect from server
    db.close()

if __name__ == '__main__':
    basic_connection();

