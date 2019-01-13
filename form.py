from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms import validators
from wtforms.validators import DataRequired, Length, NumberRange
from markupsafe import Markup


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    town = StringField("Town", validators=[DataRequired()])
    weight = IntegerField('Weight', validators=[DataRequired(), Length(min=2, max=20)])
    height = IntegerField('Height', validators=[DataRequired()])
    submit = SubmitField('Register')


class CalCount(FlaskForm):
    one = IntegerField('Calorie1', validators=[NumberRange(min=0)])
    two = IntegerField('Calorie2', validators=[NumberRange(min=0)])
    three = IntegerField('Calorie3', validators=[NumberRange(min=0)])
    submit = SubmitField('submit')


class UpdateProfile(FlaskForm):
    id = StringField("Username")
    town = StringField("Town")
    weight = IntegerField("Weight", validators=[NumberRange(min=0)])
    height = IntegerField("Height", validators=[NumberRange(min=0)])
    submit = SubmitField('submit')


class Password(FlaskForm):
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Re-enter Password')

