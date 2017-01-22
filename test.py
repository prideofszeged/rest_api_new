import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABlE if not exists users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'jose', 'asdf')

insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert_query, user)

users = [
    (2, 'jeb', 'asdf'),
    (3, 'joe', 'asdf')
]

cursor.executemany(insert_query, users)

select_query = "Select * from users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()

connection.close()