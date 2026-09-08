# Conditional statement
import getpass

user = 'ciaa'
password = 'mamamo'

u = input( 'Enter user ---> ' )
p= getpass.getpass ( 'Enter password ---> ')

if u == user and p == password: 
	 print( ' ACCESS GRANTED ' )
else:
	 print( ' ACCESS DENIED ' )
