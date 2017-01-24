import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

#user INTEGER for autoincrement instead of int
create_table = "CREATE TABlE if not exists users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABlE if not exists items (id INTEGER PRIMARY KEY, name text , price real)"
cursor.execute(create_table)
#cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

connection.commit()

connection.close()