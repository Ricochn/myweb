from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField("usrname:", validators=[DataRequired()])
    password = PasswordField("password:", validators=[DataRequired()])
    submit = SubmitField('Login')
