#a user registration and login 
import time
users = {}
status = ""
 #a user chooses from the available options whether registered or not, inorder to continue
def displayMenu():
    status = input("if you are a new user, type 'yes' to continue if registered type 'not'. To quit, pres 'exit' ")
    if status == "yes":
        UserExists()
    elif status == "not":
        NoRecords()
 #if a user exist, she or he can log in
def UserExists():
    EnterUsername = input("enter your username: ")
 
    if EnterUsername in users:
        print("\nLogin name already exist!\n")
    else:
        EnterPassword = input("Enter password: ")
        users[EnterUsername] = EnterPassword
        print("\n New User Acount succcesfuly Created\n")
 #if a user does notexist, she or he can create an account
def NoRecords():
    login = input("Enter Username here: ")
    passw = input("Enter password here: ")
 
    if login in users and users[login] == passw:
        print("\n succesfuly logged in \n")
    else:
        print("\n UserName or password is invalid! please try again\n")
 
while status != "exit":
    displayMenu()
