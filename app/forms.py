from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class InsertOratorForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(10, 110)])
    job = StringField('Job', validators=[DataRequired()])
    info = TextAreaField('Information', validators=[DataRequired()])
    photo = StringField('Photo Url') # ainda não sei se damos url ou opcao de upload
    submit = SubmitField('Add Orator')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
