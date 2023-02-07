#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('users.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE USERS
         (ID INTEGER PRIMARY KEY AUTOINCREMENT,
         NAME        TEXT NOT NULL,
         SURNAME     TEXT NOT NULL,
         EMAIL       TEXT NOT NULL,
         PASSWORD    TEXT NOT NULL);''')
        
conn.execute("INSERT INTO USERS VALUES(NULL, 'Jose', 'Poveda', 'Jose.poveda@utrgv.edu', 'python' );")  
conn.execute("INSERT INTO USERS VALUES(NULL, 'Tony', 'Connors', 'Tony.connors@utrgv.edu', 'tony' );")   
conn.execute("INSERT INTO USERS VALUES(NULL, 'Allen', 'Key', 'Allen.Key@utrgv.edu', 'allen' );") 
conn.execute("INSERT INTO USERS VALUES(NULL, 'Christian', 'Nodal', 'Christian.Nodal@utrgv.edu', 'christian' );")
conn.execute("INSERT INTO USERS VALUES(NULL, 'Alice', 'Wonderland', 'Alice.Wonderland@utrgv.edu', 'alice' );")
conn.execute("INSERT INTO USERS VALUES(NULL, 'Kevin', 'Costner', 'Kevin.Costner@utrgv.edu', 'kevin' );")
conn.execute("INSERT INTO USERS VALUES(NULL, 'Christ', 'Colombus', 'Christ.Colombus@utrgv.edu', 'Christ' );")


conn.commit()
print ("Records created successfully")
conn.close()
