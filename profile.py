import os
from flask import Flask, render_template, request

app = Flask(__name__, static_folder='images')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template('profile.html')


@app.route('/upload', methods='[POST]')
def upload():
    image = os.path.join(APP_ROOT, 'images/')

    if not os.path.isdir(image):
        os.mkdir(image)

    for upload in request.files.getlist('file'):
        filename = upload.filename
        destination = '/'.join([image, filename])
        upload.save(destination)

    return render_template('profile.html', image_name=filename)


if __name__ == '__main__':
    app.run(debug=True)
