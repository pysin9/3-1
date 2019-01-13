from wtforms import StringField, SubmitField, Form, PasswordField, IntegerField, BooleanField
from wtforms import validators
from wtforms.validators import email, DataRequired, NumberRange
from markupsafe import Markup

class LoginForm(Form):
    id = StringField("Username", [validators.DataRequired('Please enter your name.')])
    password = PasswordField("Password", [validators.DataRequired('Please enter your password.')])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(Form):
    id = StringField("Username", [validators.DataRequired('Please enter your name.')])
    password = PasswordField("Password", [validators.DataRequired('Please enter your password.')])
    town = StringField("Town", [validators.DataRequired("Please enter your location.")])
    weight = IntegerField("Weight", [validators.DataRequired("Please enter your weight in kilogram")])
    height = IntegerField("Height", [validators.DataRequired("Please enter your height in meters")])
    submit = SubmitField('Register')


class ResetForm(Form):
    email = StringField("Email", validators=[DataRequired(), email()])
    submit = SubmitField("Send Email")

class CalCount(Form):
    one = IntegerField('Calorie1', validators=[NumberRange(min=0)])
    two = IntegerField('Calorie2', validators=[NumberRange(min=0)])
    three = IntegerField('Calorie3', validators=[NumberRange(min=0)])
    submit = SubmitField('submit')


class UpdateProfile(Form):
    id = StringField("Username")
    town = StringField("Town")
    weight = IntegerField("Weight", validators=[NumberRange(min=0)])
    height = IntegerField("Height", validators=[NumberRange(min=0)])
    submit = SubmitField('submit')


class Password(Form):
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Re-enter Password')

