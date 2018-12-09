from flask import Flask, render_template, flash , url_for , redirect
from form import *
from user import *
from flask import request


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if request.method == 'POST':
        users = get_user(login_form.id.data, login_form.password.data)
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



if __name__ == "__main__":
    app.run(debug=True)