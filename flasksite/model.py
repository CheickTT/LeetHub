from flask_sqlalchemy import SQLAlchemy
from flasksite import app, db, login_manager
from flask_login import UserMixin
from pychartjs import BaseChart, ChartType, Color, Options


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


class MyChart(BaseChart):

    type = ChartType.Bar
    callback = "<<myJavascriptFunction>>"
    inlineJS = "<<function(value, index, values) {return '$' + value;} >>"

    class labels:
        group = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    class data:

        class apples: 
            data = [2, 8, 11, 7, 2, 4, 3]
            backgroundColor = Color.Palette(Color.Hex('#30EE8090'), 7, 'lightness')
            borderColor = Color.Green
            yAxisID = 'apples'