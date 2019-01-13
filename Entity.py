from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import case
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class MapPlace(db.Model):
    __tablename__ = 'MapPlace'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Picture = db.Column(db.String(128))
    Color= db.Column(db.String(32))
    Longitude = db.Column(db.Integer)
    Latitude = db.Column(db.Integer)
    Location = db.Column(db.String(2083))
    Category = db.Column(db.String(64))
    Postal_Code = db.Column(db.String(32))

    @hybrid_property
    def Cate(self):
        if self.Color == "#8C4C80":
            return self.Category == "Healthy"


if __name__ == '__main__':
    manager.run()
