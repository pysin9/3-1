from flask import Flask, render_template, request
from calcount import Calories
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('calcount.html')


def updatecalories():
    cal1 = request.form['calone']
    cal2 = request.form['caltwo']
    cal3 = request.form['calthree']
    c = Calories(cal1, cal2, cal3)
    return c


if __name__ == '__main__':
    app.run()
