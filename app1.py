from flask import Flask, render_template
from form import *
from user import *
app = Flask(__name__)


@app.route("/")
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


@app.route("/register")
def register():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)