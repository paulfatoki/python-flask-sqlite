#Description: This python script assumes that you already have
# a database.db file at the root of your workspace.
# This python script will CREATE a table called students 
# in the database.db using SQLite3 which will be used
# to store the data collected by the forms in this app
# Execute this python script before testing or editing this app code. 
# Open a python terminal and execute this script:
# python new_table.py

import sqlite3


conn = sqlite3.connect('database.db')
print("database connectd ...")

conn.execute('DROP TABLE IF EXISTS students')

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, zip TEXT)')


print("Created table successfully!")

conn.close()

