from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class RegisterForm(FlaskForm):
    username = StringField('user name', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired(), Length(min=8, max=20)])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    username = StringField('user name', validators=[DataRequired(), Length(min=2, max=30)])
    password = StringField('password', validators=[DataRequired(), Length(min=8, max=20)])
    login = SubmitField('login')


