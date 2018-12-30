from flask import Flask, render_template, request, flash, redirect, url_for
from calcount import *
from form import *
from wtforms import *
app = Flask(__name__)
app.secret_key = "secret"
app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/calcount', methods=['GET', 'POST'])
def calcount():
    form = CalCount(request.form)
    result = 0
    try:
        if request.method == 'POST':
            result = Calories(int(request.form['calorie1']), int(request.form['calorie2']), int(request.form['calorie3']))
    except ValueError:
        flash('Please enter an integer')
    store = result
    return render_template('calcount.html', form=form, result=result, store=store)


@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = 0
    form = UpdateProfile(request.form)
    if request.method == 'POST':

        bmi = float(request.form['weight'])/(float(request.form['weight'])*float(request.form['weight']))
    return render_template('profile.html', bmi=bmi, form=form)


if __name__ == '__main__':
    app.debug = True
    app.run()
