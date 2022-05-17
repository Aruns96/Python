Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# import mysql connector
# connect to the database by entering the details
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', password='provide your password')
# creating a new database
mycursor = db.cursor()
mycursor.execute('create database ab')


#  To show the databases name
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', password='Arun@1996')
mycursor = db.cursor()
mycursor.execute('show databases')
for x in mycursor:
    print(x)



# To create a new table
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', password='Arun@1996',database='ab')
mycursor = db.cursor()
mycursor.execute('create table jb(name varchar(20),job  varchar (25)) ')



# To show the table
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', password='Arun@1996',database='ab')
mycursor = db.cursor()
mycursor.execute('show tables')
for x in mycursor:
    print(x)

# To add some data to the table
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', password='Arun@1996', database='ab')
mycursor = db.cursor()
a = 'insert into jb(name,job) values (%s,%s)'
b = [('rahul', 'driver'), ('sam', 'painter'), ('tom', 'carpenter')]
mycursor.executemany(a,b)
db.commit()


# To fetch one corresponding data
import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', password='Arun@1996', database='ab')
mycursor = db.cursor()
mycursor.execute('select name from jb')
out = mycursor.fetchone()
for x in out:
    print(x)


# To get all data

import mysql.connector
db = mysql.connector.connect(host='localhost', user='root', password='Arun@1996', database='ab')
mycursor = db.cursor()
mycursor.execute('select * from jb')
out = mycursor.fetchall()
for x in out:
    print(x)

