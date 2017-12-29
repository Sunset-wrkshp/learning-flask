from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
    first_name = StringField('First name', validators=[DataRequired("Put YO Name")])
    last_name = StringField('Last name', validators=[DataRequired("PUT YOUR LAST NAMAE")])
    email = StringField('Email', validators=[DataRequired("I won't spam you I promise"), Email("PUT A REAL EMAIL")])
    password = PasswordField('Password', validators=[DataRequired("DO IT"), Length(min=6, message="Think harder man")])
    submit = SubmitField('Sign up')
