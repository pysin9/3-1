from flask import Flask, render_template, flash, url_for, redirect, session
from form import *
from user import *
from flask import request


app = Flask(__name__)
SECRET_KEY = "yeah, not actually a secret"
DEBUG = True
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        if is_valid(email, password):
            session['email'] = email
            return redirect(url_for('userprofile'))
        else:
            error = 'Invalid UserId / Password'
            return render_template('login.html', error=error)
    return render_template("login.html")


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST'and form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        town = request.form['town']
        weight = request.form['weight']
        height = request.form['height']
        with sqlite3.connect('users.db') as con:
            try:
                cur = con.cursor()
                cur.execute(
                    'INSERT INTO users (username, password, town, weight, height) VALUES (?, ?, ?, ?, ?)',
                    (username, hashlib.md5(password.encode()).hexdigest(), town, weight, height))
                con.commit()

                msg = "Registered Successfully"
            except:
                con.rollback()
                msg = "Error occured"
        con.close()
        return render_template("login.html", error=msg)
    return render_template("signup.html")


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
    else:
        return render_template("reset.html")


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)