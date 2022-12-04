from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from doctor.login import User


class LoginForm(FlaskForm):
    email = StringField(label='email',validators=[DataRequired()])
    password = StringField(label='password',validators=[DataRequired()])
    submit = SubmitField(label='Signin')