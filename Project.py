from flask import *
from dbModel import *
from flask import Flask, render_template, flash, url_for, redirect, session
from form import *
from user import *
from flask import request

app = Flask(__name__)


@app.route('/')
def map():
    return render_template("Homepagee.html")


@app.route('/ingredient')
def ingredient():
    return render_template('ingredients.html')


@app.route('/userprofile')
def userprofiel():
    return render_template('userprofile.html')


@app.route("/map")
def index():
    return render_template('map.html')


app.route('/calcount', methods=['GET'])
def calcount():
    form = CalCount(request.form)
    #cal1 = form.calone
    #cal2 = form.caltwo
    #cal3 = form.calthree
    #c = Calories(cal1, cal2, cal3)
    return render_template('calcount.html',form=form)


SECRET_KEY = "yeah, not actually a secret"
DEBUG = True
app.config['SESSION_TYPE'] = 'filesystem'


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
    db_data = MapPets.query.all()
    infornation_dic = {}
    infornation_list = []
    for data in db_data:
        infornation_dic['data'] = []
        infornation_dic['Name'] = data.Name
        infornation_dic['Picture'] = data.Picture
        infornation_dic['Color'] = data.Color
        infornation_dic['Longitude'] = data.Longitude
        infornation_dic['Latitude'] = data.Latitude
        infornation_list.append(infornation_dic)
        infornation_dic = {}

    return json.dumps(infornation_list)


if __name__ == '__main__':
    app.run(debug=True)
