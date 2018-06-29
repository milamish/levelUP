#a user registration and login 
import time
users = {}
status = ""
 #a user chooses from the available options whether registered or not, inorder to continue
def display_menu():
    status = input("if you are a new user, type 'yes' to continue if registered type 'not'. To quit, pres 'exit' ")
    if status == "yes":
        User_exists()
    elif status == "not":
        No_records_exists()
 #if a user exist, she or he can log in
def User_exists():
    EnterUsername = input("enter your username: ")
 
    if EnterUsername in users:
        print("\nLogin name already exist!\n")
    else:
        EnterPassword = input("Enter password: ")
        users[EnterUsername] = EnterPassword
        print("\n New User Acount succcesfuly Created\n")
 #if a user does notexist, she or he can create an account
def No_records_exists():
    login = input("Enter Username here: ")
    passw = input("Enter password here: ")
 
    if login in users and users[login] == passw:
        print("\n succesfuly logged in \n")
    else:
        print("\n UserName or password is invalid! please try again\n")
 
while status != "exit":
    display_menu()

    session=session.Session()
    login=session['User_exists']
    
