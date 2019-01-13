from flask import *
from dbModel import *
from flask import Flask, render_template, flash, url_for, redirect, session, request
from form import *
from user import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Homepagee.html")


@app.route('/ingredient')
def ingredient():
    return render_template('ingredients.html')


@app.route('/userprofile')
def userprofile():
    return render_template('userprofile.html')


@app.route("/map" ,methods=['GET','POST'])
def map():
    data = MapPlace.query.all()
    return render_template('map.html', data=data )


@app.route("/login", methods=['GET', 'POST'])
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


@app.route("/api", methods=['POST'])
def api():
    db_data = MapPlace.query.all()
    information_dic = {}
    information_list = []
    for data in db_data:
        information_dic['data'] = []
        information_dic['Name'] = data.Name
        information_dic['Picture'] = data.Picture
        information_dic['Color'] = data.Color
        information_dic['Longitude'] = data.Longitude
        information_dic['Latitude'] = data.Latitude
        information_dic['Location'] = data.Location
        information_dic['Category'] = data.Category
        information_dic['Postal_Code'] = data.Postal_Code
        information_list.append(information_dic)
        information_dic = {}

    return json.dumps(information_list)


if __name__ == '__main__':
    app.run(debug=True)
