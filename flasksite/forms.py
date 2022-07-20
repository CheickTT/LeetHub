from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_sqlalchemy import SQLAlchemy
from flasksite.model import User
from flasksite.file_convert import get_college_list


class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  colleges = get_college_list()
  school = SelectField('College', choices=colleges)
  grad_year = DateField('Graduation Year', validators=[DataRequired(message="Year must be in YYYY format.")], format='%Y')
  print(type(grad_year))
  password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
    user_obj = User.query.filter_by(username=username.data).first()
    if user_obj:
      raise ValidationError("Username already in use.")

  def validate_email(self, email):
    user_obj = User.query.filter_by(email=email.data).first()
    if user_obj:
      raise ValidationError("Email already in use.")    


class LoginForm(FlaskForm):
  existing_user = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  existing_pass = PasswordField('Password', validators=[DataRequired()])
  login = SubmitField('Log In')  
  github_login = SubmitField('Log In with GitHub')
