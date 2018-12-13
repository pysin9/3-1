from flask import Flask, render_template, request
from calcount import *
from form import *

app = Flask(__name__)


@app.route('/calcount', methods=['GET'])
def calcount():
    form = CalCount(request.form)
    #cal1 = form.calone
    #cal2 = form.caltwo
    #cal3 = form.calthree
    #c = Calories(cal1, cal2, cal3)
    return render_template('calcount.html',form=form)

if __name__ == '__main__':
    app.run()


