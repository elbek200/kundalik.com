from database import *
from database2 import *
from utils import *

def login():
    username = input('Username : ')
    password = input('Password : ')
    
    pk = login_user(username, password)
    if pk :
         print ("welcome")
         sd = is_admin(username)
         if sd :
              admin()
         else :
              oquvchi(username)
                   
    else :
         print ("You are not registered")
    return pk

def register():
    data = dict(
        first_name = input('First Name : '),
        last_name = input('Last Name : '),
        username = input('Username :'),
        password1 = input('Password1 : '),
        password2 = input('Password2 : '),
        birth_day = input('yyyy-MM-dd :'),
        phone_number = input('+998XXXXXXXXX :')
    )
    if data['password1'] == data['password2']:
         pk = register_user(data)
         print ("successfull")
         oquvchi(data['username'])
    else :
         print ("Error password2")
         return 
    
    return pk

n = input("[1] - Login , [2] - Register \n --> :")
if n == "1":
     login()
elif n == "2":
     register()
else :
     print ("Error code")






