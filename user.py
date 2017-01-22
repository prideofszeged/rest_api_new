import sqlite3

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



