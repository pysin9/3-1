from wtforms import StringField, SubmitField, Form, PasswordField, IntegerField, BooleanField
from wtforms import validators


class LoginForm(Form):
    name = StringField('UserName', [validators.DataRequired('Please enter your name.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(Form):
    name = StringField('UserName', [validators.DataRequired('Please enter your name.')])
    password = PasswordField('Password', [validators.DataRequired('Please enter your password.')])
    town = StringField('Town', [validators.DataRequired("Please enter your location.")])
    weight = IntegerField('Weight', [validators.DataRequired("Please enter your weight in kilogram")])
    height = IntegerField('Height', [validators.DataRequired("Please enter your height in meters")])
    submit = SubmitField('Register')
