from flask import Flask,session,render_template,request

app=Flask('_name_')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home_page():
    return render_template('index.html')
def __init__(self):
        self.username= username
        self.emailadress=emailadress
        self.password= password
        db={}
        db.update(self,username,emailadress,password)

@app.route('/register', methods=['GET','POST'])
def register(self):
    if request.method=='GET':
        return render_template('register.html',title='Sign UP',form=form)
        db.update({self,username,emailadress,password}) 
        self.username=input('enter your username')
        self.emailadress=input('enter username')
        self.password=input('enter password')
       

@app.route('/login',methods=['GET','POST'])
def login(self):
    if request.method=='GET':
     return render_template('login.html',title='sign In')
    if self.password==db[self.username]:
            print('login succesful')
            
    else:
            print('try again')
            return render_template('login.html',title='sign In')
               
if __name__== '__main__':
 app.run(debug= True, port= 5059)