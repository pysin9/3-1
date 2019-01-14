import sqlite3

conn = sqlite3.connect('users.db')

conn.execute('''CREATE TABLE users 
                (username TEXT NOT NULL UNIQUE , 
                        password INTEGER ,
                        town TEXT,
                        weight FLOAT,
                        height FLOAT
                        )''')

conn.close()