import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()
create_table = "CREATE TABLE users (id int,username text,password text)"

cursor.execute(create_table)

user = (1,'jose','asdf')

insert_Query = "Insert into users values (?,?,?)"

cursor.execute(insert_Query,user)

users =[
    (2,'Bob','sed'),
    (3,'john','jsd'),
    (4,'jacob','rtfg')

]

cursor.executemany(insert_Query,users)

select_Query = "SELECT * from users"

for row in cursor.execute(select_Query):
    print(row)

connection.commit()
connection.close()