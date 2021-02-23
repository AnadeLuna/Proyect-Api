from pymongo import MongoClient
client = MongoClient()

users = client.Tinder.users
message = client.Tinder.message 


#Functions user's collection.
def read_all_users():
    filt = {}
    proyect = {"_id":0}
    result = users.find(filt,proyect)
    return list(result)

def read_one_users(name):
    filt = {"Name":str(name)}
    proyect = {"_id":0}
    result = users.find(filt,proyect)
    return list(result)



#Functions message's collection.
def read_all_message():
    filt = {}
    proyect = {"_id":0}
    result = message.find(filt,proyect)
    return list(result)

def read_one_match(match):
    filt = {"Match":str(match)}
    proyect = {"_id":0}
    result = message.find(filt,proyect)
    return list(result)

def read_one_message(messa):
    filt = {"Message":str(messa)}
    proyect = {"_id":0}
    result = message.find(filt,proyect)
    return list(result)



#Funtion to insert a user.
def insert_users(name,age,sex,lookingfor):
    dic = {"Name":f"{name}",
      "Age":f"{age}",
      "Sex":f"{sex}",
      "Looking for":f"{lookingfor}"}
    return users.insert_one(dic)



#Funtion to insert a user a message.
def insert_message(name,messa,match):
    dic_mes = {"Name":f"{name}",
      "Message":f"{messa}",
      "Match":f"{match}"}
    return message.insert_one(dic_mes)



#Funtion to delete a user.
def delete_user(name,age,sex,lookingfor):
    dic = {"Name":f"{name}",
      "Age":f"{age}",
      "Sex":f"{sex}",
      "Looking for":f"{lookingfor}"}
    return users.remove(dic)



#Funtion to delete a message.
def delete_message(name,messa,match):
    dic_mes = {"Name":f"{name}",
      "Message":f"{messa}",
      "Match":f"{match}"}
    return message.remove(dic_mes)
