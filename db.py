import random
import sqlite3




conn = sqlite3.connect('users.db')
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE users
#             	(id INTEGER PRIMARY KEY, username TEXT, balance INTEGER)''')

balance=random.sample(list(range(5000,15000)),3)

users=["Oleg","Vladimir","Aleksey"]
for index,user in enumerate(users):
    cursor.execute('INSERT INTO users (username,balance) VALUES (?,?)',(user, balance.pop(index)))
    conn.commit()
