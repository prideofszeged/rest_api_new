import sqlite3
from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        #id is python keyword thus the underscore
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "Select * from users where username=?"

        #has to be in form of a tuple with comma
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            #id, username, password
            #positional arguments
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "Select * from users where id=?"

        #has to be in form of a tuple with comma
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            #id, username, password
            #positional arguments
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank"
                        )
    def post(self):
        data = UserRegister.parser.parse_args()


        if User.find_by_username(data['username']):
            return {'message': "A user with name '{}' already exists.".format(data['username'])}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "Insert INTO users VALUES (NULL, ?, ?)"

        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201




