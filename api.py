from flask import Flask
from flask import request
from bson import json_util
from flask import jsonify
from mongoConnection import read_all_users,read_one_users
from mongoConnection import read_all_message, read_one_match, read_one_message 
from mongoConnection import insert_users, insert_message
from mongoConnection import delete_user, delete_message

app = Flask(__name__)

#Welcome Funtion.
@app.route("/")
def root():
    return "Hello, you are in Gossip Girl of Tinder."


#Functions that search the users collection.
@app.route("/users")
def users():
    data = read_all_users()
    return jsonify(data)

@app.route("/users/<name>")
def user(name):
    data = read_one_users(name)
    return jsonify(data)



#Functions that search the collection message.
@app.route("/message")
def messages():
    data = read_all_message()
    return jsonify(data)

@app.route("/message/<match>")
def matchs(match):
    data = read_one_match(match)
    return jsonify(data)

@app.route("/message/<messa>")
def messag(messa):
    data = read_one_message(messa)
    return jsonify(data)



#Funtion to create users.
@app.route("/users/new/<name>/<age>/<sex>/<lookingfor>")
def insert_user(name,age,sex,lookingfor):
    data = read_one_users(name)
    if len(data) > 0:
        return "This users is allready exist. Please enter a new one."
    else:
        insert_users(name,age,sex,lookingfor)
        return "The user has been created successfully."



#Funtion to create message.
@app.route("/message/new/<name>/<messa>/<match>")
def insert_messages(name,messa,match):
    data = read_one_message(messa)
    if len(data) > 0:
        return "This message is allready exist. Please enter a new one."
    else :
        insert_message(name,messa,match)
        return "The message has been created successfully."




#Funtion to delete users.
@app.route("/users/delete/<name>/<age>/<sex>/<lookingfor>")
def delet_user(name,age,sex,lookingfor):
    data = read_one_users(name)
    if len(data) > 0:
        delete_user(name,age,sex,lookingfor)
        return "The user has been removed."
    else:
        return "The user not exist. Test to remove an existing user."



#Funtion to delete message.
@app.route("/message/delete/<name>/<messa>/<match>")
def delet_message(name,messa,match):
    data = read_one_message(messa)
    if len(data) > 0:
        delete_message(name,messa,match)
        return "The message has been removed."
    else:
        return "The message not exist. Test to remove an existing message."


app.run(debug=True)
