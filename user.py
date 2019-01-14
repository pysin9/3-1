import sqlite3, hashlib
from flask import session


def is_valid(username, password):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('SELECT username, password FROM users')
    data = cur.fetchall()
    for row in data:
        if row[0] == username and row[1] == hashlib.md5(password.encode()).hexdigest():
            return True
    return False


def getLoginDetails():
    with sqlite3.connect('users.db') as conn:
        cur = conn.cursor()
        if 'username' not in session:
            loggedIn = False
        else:
            loggedIn = True
            cur.execute("SELECT username FROM users WHERE username = ?", (session['username'], ))
            username = cur.fetchone()
    conn.close()
    return (loggedIn, username)