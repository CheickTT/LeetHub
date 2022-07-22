from flask_sqlalchemy import SQLAlchemy,sqlalchemy
from flasksite import app, db, login_manager, postdb
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
  github_access_token = db.Column(db.String(255), nullable=False, default='testtoken')


  def __repr__(self):
    return f"User('{self.username}', '{self.email}', '{self.profile_pic}', '{self.school}', '{self.grad_year}', '{self.password_hash}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    profile_pic = db.Column(db.String(20), nullable=False, default='default.png')
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)

    def __str__(self):
      return f"Post('{self.username}', '{self.title}', '{self.profile_pic}','{self.description}')"


class MyChart(BaseChart):

    type = ChartType.Bar

    class labels:
        group = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    class data:

        class submission: 
            data = [7]
            backgroundColor = Color.Palette(Color.Hex('#30EE8090'), 7, 'lightness')
            borderColor = Color.Green
            yAxisID = 'submission'
            
    class options: 

        title = Options.Title("Number of Submissions")

        scales = {
            "yAxes": [
                {"id": "submission",
                 "ticks": {
                     "beginAtZero": True,
                     "callback": "<<function(value, index, values) {return value ;}>>",
                     },
                  "scaleLabel": {
                      "display": True,
                      "labelString": "Submissions"
                  }
                }
            ],
            "xAxes": [{
                  "scaleLabel": {
                      "display": True,
                      "labelString": "Dates"
                  }
                }
            ]
        }

class circleChart(BaseChart):

    type = ChartType.Doughnut

    class labels:
        group = ['Easy', 'Medium', 'Hard']


    
    class data:

        class submission: 
            data = [7]
            backgroundColor = ["green","orange","red","blue","brown","cyan","yellow","indigo","purple","pink","violet"]
            
    class options: 

        title = Options.Title("Number of Submissions")
