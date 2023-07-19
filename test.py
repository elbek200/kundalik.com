from databases import create_table_user, insert_user , login , activate_user
import random
from qwerty import send_email

print ("---------------- Login or Register --------------------")
n = input ("\nRegister - [1]\n Login - [2]\n ENTER --> :")
def login2():
    user = dict(
        username = input('Username : '),
        password = input('Password :'),
    )
    response = login (user)
    if response:
        print ("welcome" , user["username"])
    else :
        print ("invalid username or password!!!")

def registor():
   data = dict(
   first_name = input("Enter your first name: "),
   last_name = input("Enter your last name: "),
   email = input("Enter your email: "),
   username = input("Enter your username: "),
   password1 = input("Enter your password: "),
   password2 = input("Password confirm: ")
   )   
   response = insert_user(data)
   if response == 201:
       code = random.randint(1000,9999)
       send_email(data["email"] , code)
       verifycation = input("code :")
       if verifycation == f"{code}":
           activate_user(data["username"])
           print ("done")
       else :
           print ("error")
if n == "1":
    registor()
elif n == "2":
    login2()
else:
    print ("Error !!!")
if __name__ == '__main__':
    create_table_user()