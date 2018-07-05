from flask import Flask
from flask import *
from views import user
from db import db
from test_register import test_password 

db={}
app=Flask(__name__)
app.secret_key="mish"


@app.route("/")
def home():
    if not session.get('logged_in'):
        return "<h4><a href = '/login'></b>" + \
          "login</b></a><br><br><a href = '/register'>register</a></h4>" 
    else:
         return ("helo'" + username +"'")


@app.route("/login", methods=['POST','GET'])
def login():
    return render_template('login.html',title='sign Up',form=register)
    if request.form['password'] == 'password' and request.form['username'] == 'username':
        session['logged_in'] = True
    else:
        flash('wrong password!')
   
    

@app.route("/register",methods=['POST','GET'])
def register():
        return render_template('register.html',title='Sign UP',form=register)  
        emailadress=request.form['emailadress']
        username=request.form['username']
        password=request.form['password']
        repeatpassword=request.form['repeatpassword']
        db.update({db:[username,emailadress,password,repeatpassword]}) 
        session['db']=db
        print ("your username a is '" + username + "'")

@app.route("/db")
def db():
       db={}
       db.update({db:[username,emailadress,password,repeatpassword]})
       print("db updated'" + db + "'")
       return  render_template('db.html',title='database',form=db)
       
@app.route("/comment")
def user_comment():
    if request.form['username'] in db:
        session['username']=request.form['username']    
        return render_template('index.html')
    else:
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()  


if __name__ =="__main__":
    app.run(debug=True)
