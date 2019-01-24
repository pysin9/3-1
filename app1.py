from flask import *
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = 'secret secret'
DEBUG = True


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', False)
        password = request.form.get('password', False)
        if is_valid(username, password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            msg = 'Invalid UserId / Password'
            return render_template('login.html', error=msg)
    return render_template("login.html")


def is_valid(username, password: str):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('SELECT password FROM users WHERE username = ?', (username,))
    data = cur.fetchone()
    if hashlib.sha256(password.encode()).hexdigest() == data[0]:
        return True
    return False


@app.route("/register/", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', False)
        password = request.form.get('password', False)
        town = request.form.get('town', False)
        weight = request.form.get('weight', False)
        height = request.form.get('height', False)
        with sqlite3.connect('users.db') as con:
            try:
                cur = con.cursor()
                cur.execute(
                    'INSERT INTO users (username, password, town, weight, height) VALUES (?, ?, ?, ?, ?)',
                    (username, sha256_crypt.encrypt(password), town, weight, height))
                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()
        return render_template("login.html", error=msg)
    return render_template("signup.html")

@app.route("/registerForm")
def registrationForm():
    return render_template("signup.html")


@app.route("/loginForm")
def loginForm():
    if 'email' in session:
        return redirect(url_for('userprofile'))
    else:
        return render_template('login.html', error='')

@app.route("/reset")
def reset():
        if 'username' not in session:
            return redirect(url_for('login'))
        if request.method == "POST":
            oldPassword = request.form['oldpassword']
            oldPassword = hashlib.md5(oldPassword.encode()).hexdigest()
            newPassword = request.form['newpassword']
            newPassword = hashlib.md5(newPassword.encode()).hexdigest()
            with sqlite3.connect('users.db') as conn:
                cur = conn.cursor()
                cur.execute("SELECT username, password FROM users WHERE username = ?", (session['username'],))
                username, password = cur.fetchone()
                if password == oldPassword:
                    try:
                        cur.execute("UPDATE users SET password = ? WHERE username = ?", (newPassword, username))
                        conn.commit()
                        flash("Changed successfully", 'success')
                    except:
                        conn.rollback()
                        flash("Failed", 'danger')
                    return render_template("reset.html")
                else:
                    flash("Wrong password", 'danger')
            conn.close()
            return render_template("reset.html")
        return render_template("reset.html")



if __name__ == "__main__":
    app.run(debug=True)