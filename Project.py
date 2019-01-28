from flask import render_template, url_for, redirect, request, session, flash, redirect, url_for, send_from_directory
from dbModel import *
from Entity import MapPlace
from form import *
from calcount import *
import sqlite3
import hashlib

import simplejson as json

app = Flask(__name__)
app.secret_key = 'secret secret'
app.config['SESSION_TYPE'] = 'filesystem'

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
def map():
    data = MapPlace.query.all()
    return render_template('map.html', data=data)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    with sqlite3.connect('users.db') as con:
        cur = con.cursor()
        cur.execute('SELECT town FROM users WHERE username = ?', (session['username'],))
        fetchtown = cur.fetchone()
        sestown = fetchtown[0]

        cur.execute('SELECT height FROM users WHERE username = ?', (session['username'],))
        fetchheight = cur.fetchone()
        sesheight = fetchheight[0]

        cur.execute('SELECT weight FROM users WHERE username = ?', (session['username'],))
        fetchweight = cur.fetchone()
        sesweight = fetchweight[0]


        sesuser = session['username']

        bmi = 0
        form = UpdateProfile(request.form)
        if request.method == 'POST':
            username = request.form['username']
            town = request.form['town']
            weight = request.form['weight']
            height = request.form['height']
            with sqlite3.connect('users.db') as con:
                try:
                    cur = con.cursor()
                    cur.execute('UPDATE users SET username=?, town=?, weight=?, height=? WHERE username=?', (username, town, weight, height, session['username']))
                    con.commit()
                    flash('Updated Successfully!')
                    session['username'] = username
                    session['town'] = town
                    session['weight'] = weight
                    session['height'] = height
                except:
                    con.rollback()
                    flash('Update Unsuccessful!')

            con.close()
            bmi = float(1) / (float(1) * float(1))
            return redirect(url_for('profile'))
    con.close()
    return render_template('profile.html', bmi=bmi, form=form, sesuser=sesuser, sestown=sestown, sesheight=sesheight, sesweight = sesweight)


def changepass():
    form = Password(request.form)
    if request.method == 'POST':
        password = request.form['newpassword']
        with sqlite3.connect('users.db') as con:
            try:
                cur = con.cursor()
                cur.execute('UPDATE users SET password=? WHERE username=?', (hashlib.sha256(password.encode()).hexdigest(), session['username']))
                con.commit()
                flash('Updated Successfully!')
            except:
                con.rollback()
                flash('Update Unsuccessful!')
        con.close()
        return redirect(url_for('profile'))
    return render_template('profile.html')



def is_valid(username, password: str):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute('SELECT password FROM users WHERE username = ?', (username,))
    data = cur.fetchone()
    if hashlib.sha256(password.encode()).hexdigest() == data[0]:
        return True
    return False

# def check_for_admin(*args, **kw):
#     username = request.form.get('username', False)
#     print(username)
#     password = request.form.get('password', False)
#     print(password)
#     if request.path.startswith('/admin'):
#         if not is_valid(session[username == "admin"], session[password == "123"] ):
#             return redirect(url_for('index'))
#         elif is_valid(session[username == "admin"], session[password == "123"] ):
#             return redirect(url_for('admin'))

@app.route("/login/", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form.get('username', False)
        password = request.form.get('password', False)
        if username == 'admin' and password == '123':
            if is_valid(username, password):
                session['username'] = username
                return redirect(url_for('admin'))
            else:
                msg = 'Invalid UserId / Password'
                return render_template('login.html', error=msg)
        else:
            if is_valid(username, password):
                session[username] = username
                return redirect(url_for('index'))

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
                    'INSERT INTO users (username,password,town,weight,height) VALUES (?, ?, ?, ?, ?)',
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
    if request.form:
        mapplace=MapPlace(Name=request.form.get("Name"),Picture=request.form.get("Picture"),Color=request.form.get("Color"),Longitude=request.form.get("Longitude"),Latitude=request.form.get("Latitude"),Location=request.form.get("Location"),Category=request.form.get("Category"),Postal_Code=request.form.get("Postal_Code"))
        db.session.add(mapplace)
        db.session.commit()
    mapplaces = MapPlace.query.all()
    print(session)
    return render_template("admin.html" ,mapplaces=mapplaces)

@app.route("/update", methods=["POST"])
def update():
    try:
        newname = request.form.get("newname")
        oldname = request.form.get("oldname")

        newpic = request.form.get("newpicture")
        oldpic = request.form.get("oldpicture")

        newcolor = request.form.get("newcolor")
        oldcolor = request.form.get("oldcolor")

        newlong = request.form.get("newlong")
        oldlong = request.form.get("oldlong")

        newlat = request.form.get("newlat")
        oldlat = request.form.get("oldlat")

        newloca = request.form.get("newname")
        oldloca = request.form.get("oldname")

        newcategory = request.form.get("newcategory")
        oldcategory = request.form.get("oldcategory")

        newcode = request.form.get("newname")
        oldcode = request.form.get("oldname")
        if oldname != newname:
            print("The old name {} and new name {}".format(oldname, newname))
            mapplace = MapPlace.query.filter_by(Name=oldname).first()
            mapplace.Name = newname
            db.session.commit()
        elif oldpic != newpic:
            mapplace = MapPlace.query.filter_by(Picture=oldpic).first()
            mapplace.Picture = newpic
            db.session.commit()
        elif oldcolor != newcolor:
            mapplace = MapPlace.query.filter_by(Color=oldcolor).first()
            mapplace.Color = newpic
            db.session.commit()
        elif oldlong != newlong:
            mapplace = MapPlace.query.filter_by(Longitude=oldlong).first()
            mapplace.Longitude = newlong
            db.session.commit()
        elif oldlat != newlat:
            mapplace = MapPlace.query.filter_by(Latitude=oldlat).first()
            mapplace.Latitude = newlat
            db.session.commit()
        elif oldloca != newloca:
            mapplace = MapPlace.query.filter_by(Location=oldloca).first()
            mapplace.Location = newloca
            db.session.commit()
        elif oldcategory != newcategory:
            mapplace = MapPlace.query.filter_by(Category=oldcategory).first()
            mapplace.Category = newcategory
            db.session.commit()
        elif oldcode != newcode:
            mapplace = MapPlace.query.filter_by(Postal_Code=oldcode).first()
            mapplace.Postal_Code = newcode
            db.session.commit()
    except Exception as e:
        print("Couldn't update")
        print(e)
    return redirect(url_for("admin"))

@app.route("/delete", methods=["POST"])
def delete():
    name = request.form.get("name")
    category = request.form.get("Category")
    mapplace = MapPlace.query.filter_by(Name=name).first() or MapPlace.query.filter_by(Category=category).first()
    db.session.delete(mapplace)
    db.session.commit()
    return redirect(url_for("admin"))

# @app.route("/deletecategory", methods=["POST"])
# def deletecategory():
#     category = request.form.get("Category")
#     mapplace = MapPlace.query.filter_by(Category=category).first()
#     db.session.delete(mapplace)
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
