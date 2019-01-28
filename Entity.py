from flask import Flask
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine('sqlite:///app.db')
Base = declarative_base(engine)
meta = Base.metadata

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

class Create_Table(Base):
    __tablename__ = 'MapPlace'
    __table_args__ = {'mysql_engine': 'InnoDB'}


    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(64))
    Picture = db.Column(db.String(128))
    Color= db.Column(db.String(32))
    Longitude = db.Column(db.Integer)
    Latitude = db.Column(db.Integer)
    Location = db.Column(db.String(2083))
    Category = db.Column(db.String(64))
    Postal_Code = db.Column(db.String(32))

Base.metadata.create_all(engine)

class MapPlace(db.Model):
    __tablename__ = 'MapPlace'

    Id = db.Column(db.Integer,unique=True, nullable=False ,primary_key=True)
    Name = db.Column(db.String(64))
    Picture = db.Column(db.String(128))
    Color= db.Column(db.String(32))
    Longitude = db.Column(db.Integer)
    Latitude = db.Column(db.Integer)
    Location = db.Column(db.String(2083))
    Category = db.Column(db.String(64))
    Postal_Code = db.Column(db.String(32))



if __name__ == '__main__':
    manager.run()
