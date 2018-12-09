from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")
def Homepage():
    return 'This is a homepage'


@app.route("/profile/<name>")
def profile(name):
    return render_template("homepage.html", name=name)

@app.route("/map")
def map():
    return render_template("map.html")


if __name__ == '__main__':
    app.run(debug=True)

d
