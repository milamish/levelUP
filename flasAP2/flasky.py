from flask import *

app=Flask(__name__)
app.secret_key="mish"
dict = {}
comments=[]

@app.route("/login", methods=['POST','GET'])
def login():
    username=request.get_json()["username"]
    password=request.get_json()["password"]
    if username in dict:
        if password==dict[username]["password"]:
            session["logged_in"]=True
            return jsonify({"message": "you have been logged in"})
        else:
            return jsonify({"message": "your password is wrong"})
    else:
        return jsonify({"message": "check your username"})
   

@app.route("/register", methods=['POST','GET'])
def register():
    name= request.get_json()['name']
    email= request.get_json()['email']
    password= request.get_json()['password']
    username=request.get_json()['username']
    dict.update({username:{"name": name,"email": email,"password": password}})
    return jsonify({"message": "you have been registered"})

@app.route("/comment", methods=['POST','GET'])
def comment():
    comment=request.get_json()["comment"]
    comments.append(comment)
    return jsonify(comment)

@app.route("/users", methods=['POST','GET'])
def users():
    return jsonify(dict) 


@app.route("/delete_comment", methods=['DELETE','GET'])
def delete_comment():
    del comments[:]
    return jsonify({"message: comment succesfuly deleted"})
  
@app.route("/retrieve_comment", methods=['GET'])
def retrieve_comment():
    if len(comments) > 0:
        return jsonify(comment)
    else:
        return jsonify({"message: no comment"})
    

if __name__ =="__main__":
    app.run(debug=True)
