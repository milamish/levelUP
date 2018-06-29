from andela import User
from register2 import user_register
class User_login:
    def UserExists(self):
        '''a user can log in if they have an existing accoun i.e they are registered  '''
        self.username = input("Enter Username here: ")
        self.password = input("Enter password here: ")
 
        if self.username in Users and Users[self.username] ==self.password:
            print("\n succesfuly logged in \n")
        else:
            print("\n UserName or password is invalid! please try again\n")
 
