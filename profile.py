from flask import Flask

app = Flask(__name__, static_folder='images')


if __name__ == '__main__':
    app.run(debug=True)
