from flask import Flask, render_template, request, redirect, url_for, flash
from calcount import *
from form import *
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
DEBUG = True
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = "secret"
UPLOAD_FOLDER = '/static/images/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


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


if __name__ == '__main__':
    app.debug = True
    app.run()
