from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_sqlalchemy import SQLAlchemy
from flasksite.model import User
from flasksite.file_convert import get_college_list
import requests


class RegistrationForm(FlaskForm):
  username = StringField('LeetCode Username', validators=[DataRequired(), Length(min=2, max=20)])
  email = StringField('Email', validators=[DataRequired(), Email()])
  colleges = get_college_list()
  school = SelectField('College', choices=colleges)
  grad_year = DateField('Graduation Year', validators=[DataRequired(message="Year must be in YYYY format.")], format='%Y')
  password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
  confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Sign Up and Connect to GitHub')
#   github_btn = SubmitField('Connect to GitHub')

  def validate_username(self, username):
    user_obj = User.query.filter_by(username=username.data).first()
    if user_obj:
      raise ValidationError("Username already in use.")
    if requests.get(" https://leetcode.com/"+username.data).status_code == 404:
      raise ValidationError("Leetcode ID does not exists. Please enter a valid Leetcode ID")

  def validate_email(self, email):
    user_obj = User.query.filter_by(email=email.data).first()
    if user_obj:
      raise ValidationError("Email already in use.")    


class LoginForm(FlaskForm):
  existing_user = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
  existing_pass = PasswordField('Password', validators=[DataRequired()])
  login = SubmitField('Log In')  



class SearchForm(FlaskForm):
  searched = StringField("Search for a profile", validators=[DataRequired()])
  search_btn = SubmitField("Search")


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    post_btn = SubmitField("Post")