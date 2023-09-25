from datetime import datetime
from schoolblog import db, login_manager
from sqlalchemy import Column, ForeignKey, String, Integer, Text, DateTime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    """
    Purpose: gets the user helps in auth
    """
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    profile_image = db.Column(db.String(64),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    pass_hash = db.Column(db.String(128))

    posts = db.relationship('Blog',backref='author',lazy=True)


    def __init__(self, email, username, password,*args, **kwargs):
        self.email = email
        self.username = username
        self.pass_hash = generate_password_hash(password)


    def check_password(self, password):
        """
        Purpose: check if password matches
        """
        return check_password_hash(self.pass_hash,password)


    def __repr__(self):
        return f"Username {self.username}"


class Blog(db.Model,UserMixin):

    users = db.relationship(User)

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)

    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.String(140),nullable=False)
    text = db.Column(db.Text,nullable=False)

    def __init__(self,title,text,user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        """
        Purpose: printing out what we got
        """
        return f"Post ID: {self.id} -- Date: {self.date} -- Title: {self.title}"

