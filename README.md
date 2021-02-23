# Proyect-Api

![portada](https://github.com/AnadeLuna/Proyect-Api/blob/main/data/gossipgirltinder.png)

------------------------------------------

I´m doing the bootcamp of Data Analytics in [Ironchack](https://www.ironhack.com/es). And this is my fourth proyect.

The objetive of this proyect is to demonstrate all i learned about [MongoDatabase](https://www.mongodb.com/es) and [Flask](https://flask.palletsprojects.com/en/1.1.x/).

This project is focused on creating your own API. It´s will be able to receive information, store it, or serve it when needed.

In this project, I have practiced:

- Flask (API creation)
- MongoDB 
- NLTK (sentiment analysis)

------------------------------------------

My Api is based on a database that contains all users and messages of an application to conect with new people. 

URL = [http://127.0.0.1:5000/]

The endpoints: 

 1º Endpoints GET

- `/users` : To search all users.
- `/users/<name>` : To search one user.
- `/message` : To search all messages.
- `/message/<match>` : To search a match and see all the conversation.
- `/message/<messa>` : To find a message and see who are involt.

2º Endpoints POST

- `/users/new/<name>/<age>/<sex>/<lookingfor>`: To create a new user.
- `/message/new/<name>/<messa>/<match>` : To create a new message.

3º Endpoints DELETE

- `/users/delete/<name>/<age>/<sex>/<lookingfor>` : To delete a user.
- `/message/delete/<name>/<messa>/<match>` : To delete a message.

-----------------------------------------

# Files

My database in mongodb is **Tinder** and the collections are **users** and **messages**.

In file **api.py** you can find my code of python using flask and in **mongoConnection.py** are the funtions to conect with mongodb which I then export to **api.py**.

In directory **testingMongoDb** and file **MongoDB** you can find all the funtions that I have tested in **jupyter notebook**.

In directory **analyzer** you can find the Sentiment Analysis of the messages in **analyzer.ipynb**.






