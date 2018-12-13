from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("Homepagee.html")


@app.route('/ingredient')
def ingredient():
    return render_template('ingredients.html')

@app.route('/userprofile')
def userprofiel():
    return render_template('userprofile.html')


if __name__ == '__main__':
    app.run()
