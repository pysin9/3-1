from flask import render_template, url_for, redirect, request, session, flash, redirect, url_for, send_from_directory
from dbModel import *
from form import *
from calcount import *
from werkzeug.utils import secure_filename
import os
import sqlite3
import hashlib
from user import is_valid
import simplejson as json
from flask.ext.cache import Cache

app = Flask(__name__)

UPLOAD_FOLDER = '/static/images/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
app.secret_key = 'Secret Secret'

@app.route('/')
def index():
    if 'username' in session:
        return render_template('userprofile.html')
    else:
        return render_template('Homepagee.html')


@app.route('/ingredient')
def ingredient():
    return render_template('ingredients.html')



@app.route("/map" ,methods=['GET', 'POST'])
@cache.cached(timeout=100)
def map():
    data = MapPlace.query.all()
    return render_template('map.html', data=data)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    bmi = 0
    form = UpdateProfile(request.form)
    if request.method == 'POST':
        bmi = float(request.form['weight'])/(float(request.form['weight'])*float(request.form['weight']))
    return render_template('profile.html', bmi=bmi, form=form)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


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


@app.route("/register", methods=['GET', 'POST'])
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


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/calcount', methods=['GET', 'POST'])
def calcount():
    form = CalCount(request.form)
    result = 0
    try:
        if request.method == 'POST':
            result = Calories(int(request.form['calorie1']), int(request.form['calorie2']),
                              int(request.form['calorie3']))
    except ValueError:
        flash('Please enter an integer')
    store = result
    return render_template('calcount.html', form=form, result=result, store=store)


if __name__ == "__main__":
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0')


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
