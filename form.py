from wtforms import StringField, SubmitField, Form, PasswordField, IntegerField, BooleanField
from wtforms import validators


class LoginForm(Form):
    id = StringField([validators.DataRequired('Please enter your name.')])
    password = PasswordField([validators.DataRequired('Please enter your password.')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(Form):
    id = StringField([validators.DataRequired('Please enter your name.')])
    password = PasswordField([validators.DataRequired('Please enter your password.')])
    town = StringField([validators.DataRequired("Please enter your location.")])
    weight = IntegerField([validators.DataRequired("Please enter your weight in kilogram")])
    height = IntegerField([validators.DataRequired("Please enter your height in meters")])
    submit = SubmitField('Register')
