#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import sqlite3

def header(title):
    print("Content-type:text/html\r\n\r\n")
    print("<html>\n<head>\n<title>%s</title>\n</head>\n<body>\n" % (title))

def footer():
    print("</body></html>")
    

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
name = form.getvalue('fname')
surname = form.getvalue('lname')
email = form.getvalue('email')
password  = form.getvalue('pswd1')

#Database users.db connection and test
conn = sqlite3.connect('users.db')
registration_query = "INSERT INTO USERS VALUES(NULL, '"+name+"', '"+surname+"', '"+email+"', '"+password+"');" 
conn.execute(registration_query)  
conn.commit()

try:
	if not form:
	   header("Login Response")
	else:
	   header("Connected ...")
	   print("<center><hr/><h3>User created. Welcome %s </h3><hr/></center>" % (name))
	   print("<h3><a href='http://127.0.0.1/login.htm'>Click here to login</a></h3>")
	   print("<h3><a href='http://127.0.0.1/registration.htm'>Click here to create a new user</a></h3>")
	   print("<h3><a href='http://127.0.0.1/cgi-bin/users_DB.py'>Click here to see the system user list</a></h3>")
    
except ValueError:
    header("No Success!")
    print("<h3>Please go back and try again.</h3>")

footer()

