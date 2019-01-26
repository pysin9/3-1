from flask import render_template, url_for, redirect, request, session, flash, redirect, url_for, send_from_directory
from dbModel import *
from Entity import MapPlace
from form import *
from calcount import *
from werkzeug.utils import secure_filename
import os
import sqlite3
import hashlib

import simplejson as json
from flask.ext.cache import Cache

app = Flask(__name__)
app.secret_key = 'secret secret'
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


def is_valid(username, password: str):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('SELECT password FROM users WHERE username = ?', (username,))
    data = cur.fetchone()
    if hashlib.sha256(password.encode()).hexdigest() == data[0]:
        return True
    return False


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', False)
        password = request.form.get('password', False)
        if is_valid(username, password):
            session['username'] = username
            return redirect(url_for('index'))

        elif is_valid(username="admin" , password="123"):
            session['username'] = "admin"
            return redirect(url_for('admin'))
        else:
            msg = 'Invalid UserId / Password'
            return render_template('login.html', error=msg)
    return render_template("login.html")


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
                    (username, hashlib.sha256(password.encode()).hexdigest(), town, weight, height))
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

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.form :
        try:
            mapplace=MapPlace(Name=request.form.get("Name"),Picture=request.form.get("Picture"),Color=request.form.get("Color"),Longitude=request.form.get("Longitude"),Latitude=request.form.get("Latitude"),Location=request.form.get("Location"),Category=request.form.get("Category"),Postal_Code=request.form.get("Postal_Code"))
            db.session.add(mapplace)
            db.session.commit()
        except Exception as e:
            print("Failed to add ")
            print(e)
    mapplaces = MapPlace.query.all()
    return render_template("admin.html" ,mapplaces=mapplaces)

@app.route("/update", methods=["POST"])
def update():
    try:
        newname = request.form.get("newname")
        oldname = request.form.get("oldname")
        newcategory = request.form.get("newcategory")
        oldcategory = request.form.get("oldcategory")
        if oldname != newname:
            print("The old name {} and new name {}".format(oldname, newname))
            mapplace = MapPlace.query.filter_by(Name=oldname).first()
            mapplace.Name = newname
            db.session.commit()
        elif oldcategory != newcategory:
            mapplace = MapPlace.query.filter_by(Category=oldcategory).first()
            mapplace.Category = newcategory
            db.session.commit()
    except Exception as e:
        print("Couldn't update")
        print(e)
    return redirect("/admin" )

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("Name")
    category = request.form.get("Category")
    if name == name :
        mapplace = MapPlace.query.filter_by(Name=name).first()
        # mapplace1 = MapPlace.query.filter_by(Category=category).first()
        db.session.delete(mapplace)
        # db.session.delete(mapplace1)
        db.session.commit()
    elif  category == category:
        category = request.form.get("Category")
        mapplace1 = MapPlace.query.filter_by(Category=category).first()
        db.session.delete(mapplace1)
    return redirect("/admin")


# def delete1():
#     category = request.form.get("Category")
#     mapplace1 = MapPlace.query.filter_by(Category=category).first()
#     db.session.delete(mapplace1)
#     db.session.commit()
#     return redirect("/admin")

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
