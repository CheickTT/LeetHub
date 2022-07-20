from flask_sqlalchemy import SQLAlchemy
from flasksite import app, db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  profile_pic = db.Column(db.String(20), nullable=False, default='default.png')
  school = db.Column(db.String(120), nullable=False)  
  grad_year = db.Column(db.String(4), nullable=False)
  password_hash = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.profile_pic}', '{self.school}', '{self.grad_year}', '{self.password_hash}')"
