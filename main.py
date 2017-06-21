import sqlite3
import getpass

conn = sqlite3.connect('firstbase.sqlite')
print "Connecting database ";

cursor1 = conn.execute("SELECT id, access, login, password  from loginlist")
for row in cursor1:
   print "id = ", row[0]
   print "access = ", row[1]
   print "login  = ", row[2]
   print "and the password is", row[3], "\n"

print "Operation was done successfully\n";

print "Now lets do the Authorization\n"

print "Enter login"
entered_login = raw_input("< ")

print "Enter password"
entered_password = getpass.getpass("< ")

cursor2 = conn.cursor()

x = cursor2.execute("SELECT * from loginlist WHERE login =:entered_login AND password =:entered_password", {"entered_login" : entered_login, "entered_password" : entered_password})

if cursor2.fetchall():
    print "Authorization WAS A HUGE SUCCESS!!"
else:
    print "You failed!"

cursor2.execute("SELECT * from loginlist WHERE login =:entered_login AND password =:entered_password", {"entered_login" : entered_login, "entered_password" : entered_password})

for row in cursor2:
    print "This user has got access to the following files:\n", row[4]

conn.close()
