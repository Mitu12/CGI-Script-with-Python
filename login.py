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
email = form.getvalue('email')
password  = form.getvalue('pswd')

#Database users.db connection and test
conn = sqlite3.connect('users.db')
login_query = "select email, password, name from USERS where email='"+email+"' and password='"+password+"';"            
cursor = conn.execute(login_query)  


r=0
email_db = ""
password_db = ""
name_db = ""
for row in cursor:
	r+=1
	    
if r > 0:
	email_db = row[0] 
	password_db = row[1]
	name_db = row[2]

try:
	if not form:
	   header("Login Response")
	elif (email == email_db and password == password_db):
	   header("Connected ...")
	   print("<center><hr/><h3>Welcome back %s </h3><hr/></center>" % (name_db))
	   print("<h3><a href='http://127.0.0.1/login.htm'>Click here to login</a></h3>")
	   print("<h3><a href='http://127.0.0.1/registration.htm'>Click here to create a new user</a></h3>")
	   print("<h3><a href='http://127.0.0.1/cgi-bin/users_DB.py'>Click here to see the system user list</a></h3>")
	   
	else:
	    header("No Success!")
	    print("<h3>Please go back and enter a valid login.</h3>")
    
except ValueError:
    header("No Success!")
    print("<h3>Please go back and enter a valid login.</h3>")

footer()






