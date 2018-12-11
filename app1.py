from flask import Flask, render_template, flash, url_for, redirect, session
from form import *
from user import *
from flask import request


app = Flask(__name__)
SECRET_KEY = "yeah, not actually a secret"
DEBUG = True
app.config['SESSION_TYPE'] = 'filesystem'


@app.route("/", methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    error = None
    if request.method == 'POST':
        user = get_user(login_form.id.data, login_form.password.data)
        if user is None:
            error = 'Wrong username and password'
        else:
            session['username'] = user.username
            return redirect(url_for('index'))
        flash(error)
    return render_template('login.html', form=login_form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        username = form.id.data
        password = form.password.data
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            create_user(username, password)
            return redirect(url_for('login'))
        flash(error)
    return render_template('signup.html', form=form)

@app.route("/reset")
def reset():
    return render_template("reset.html")

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.run(debug=True)