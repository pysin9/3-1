import sqlite3

conn = sqlite3.connect('users.db')

conn.execute('''CREATE TABLE IF NOT EXISTS users 
                (username TEXT UNIQUE , 
                        password TEXT,
                        town TEXT,
                        weight FLOAT,
                        height FLOAT
                        )''')

conn.commit()
conn.close()