import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

#user INTEGER for autoincrement instead of int
create_table = "CREATE TABlE if not exists users (id INTEGER PRIMARY KEY , username text, password text)"
cursor.execute(create_table)

connection.commit()

connection.close()