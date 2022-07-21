from flask import render_template, url_for, flash, redirect, request
# from flask_bcrypt import Bcrypt
from flasksite.forms import RegistrationForm, LoginForm, SearchForm
# from flask_behind_proxy import FlaskBehindProxy
# from flask_sqlalchemy import SQLAlchemy
from flasksite.model import User
from flasksite import app, bcrypt, db, proxied
from flask_login import login_user, logout_user, current_user, login_required
from urllib.parse import urlparse, urljoin
from sqlalchemy import or_


@app.route("/")
@app.route("/home")
def home():
  profiles = User.query.order_by(User.id.desc())
  return render_template('home.html', subtitle="Profiles", users=profiles)


@app.context_processor
def base():
  form = SearchForm()
  return dict(form=form)

@app.route("/search", methods=["POST"])
def search():
  form = SearchForm()
  if not form.validate_on_submit():
    return redirect(url_for('home'))
  else:
    search_query = form.searched.data
    user_obj = User.query.filter(or_(
      (User.username.like(f'%{search_query}%')), 
      (User.email.like(f'{search_query}%')),
      (User.school.like(f'{search_query}%')),
      (User.grad_year == f'{search_query}-01-01')
      )).all()

    return render_template("search.html", form=form, searched=search_query, users=user_obj)


@app.route("/register", methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  login_form = LoginForm()
  reg_form = RegistrationForm()
  if reg_form.validate_on_submit():
    user = User(username=reg_form.username.data, email=reg_form.email.data, school=reg_form.school.data, grad_year=reg_form.grad_year.data, password_hash=hash_pass(reg_form.password.data))
    db.session.add(user)
    db.session.commit()
    login_user(user)
    flash(f'Account created for {reg_form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', login_form=login_form, register_form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  # query the database to see if the username is present;
  # if so check for matching hash
  # if no username present reprompt;
  login_form = LoginForm()
  # reg_form = RegistrationForm()
  if login_form.validate_on_submit():
    given_user = login_form.existing_user.data # form inputs
    given_pass = login_form.existing_pass.data
    user_obj = User.query.filter_by(username=given_user).first()

    if (user_obj and bcrypt.check_password_hash(user_obj.password_hash, given_pass)):
      login_user(user_obj)        

      next = request.args.get('next')

      if not is_safe_url(next):
          return abort(400)

      flash(f'Successfully logged in as {login_form.existing_user.data}!', 'success')
      return redirect(next or url_for('home'))
    else:
      flash(f'Invalid username and/or password', 'danger')      
  return render_template('login.html', title="Login", login_form=login_form)

# @app.route("/github-login")
# def github_login():
#   return github.authorize()

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('home'))


@app.route("/profile")
@login_required
def profile():
  profile_pic = url_for('static', filename=f"img/{current_user.profile_pic}")
  return render_template("profile.html", subtitle="My Profile", profile_pic=profile_pic)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def hash_pass(password):
  pw_hash = bcrypt.generate_password_hash(password).decode('utf-8')
  return pw_hash

  