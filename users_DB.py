#!/usr/bin/python

print('Content-Type: text/html')    # HTML is following

print('')                           # require blank line between CGI header and data

# content

import sqlite3

conn = sqlite3.connect('users.db')
print("<br/><h3>Opened database successfully</h3>")

cursor = conn.execute("SELECT id, name, surname, email from USERS")


#Output data as html table
print("<table  border='1'>")
print("<tr style ='background-color:#C0C0C0;'><th>ID</th><th>First Name</th><th>Second Name</th><th>User e-mail</th></tr>")

bg=True

for row in cursor:
   if bg==True:
      print("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (row[0], row[1], row[2], row[3]))  
      bg=not(bg)
   else:
      print("<tr style ='background-color:#C0C0C0;'><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (row[0], row[1], row[2], row[3]))
      bg=not(bg)      
            
print("</table>")



print ("<br/><h3>Operation done successfully<h3>");
conn.close()
