from wtforms import SubmitField, Form, IntegerField, StringField, PasswordField
from wtforms import validators
from wtforms.validators import NumberRange


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
