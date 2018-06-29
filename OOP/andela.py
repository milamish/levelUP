class User:
    def users(self,username,emailadress,password):
        pass 
        self.username = username
        self.emailadress= emailadress
        self.password=password
    def displayMenu():
        status = input("if you are a new user, type 'yes' to continue if registered type 'not'. To quit, pres 'exit' ")
        if status == "yes":
            UserExists()
        elif status == "not":
            No_user_records()
        

