from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from The_app.api.v1.views import app_views
from The_app.db import init_db


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
init_db()

app.register_blueprint(app_views, url_prefix='/api/v1')

@app.route('/')
@app.route('/home')
def home():
    """
    Purpose: home template
    """
    return render_template('home.html')
# end def


@app.route('/login')
def login():
    """
    Purpose: login page
    """
    return render_template('login.html')
# end def


@app.route('/layout')
def layout():
    """
    Purpose: the layout
    """
    return render_template('layout.html')
# end def


@app.route('/register')
def register():
    """
    Purpose: register form
    """
    return render_template('register.html')
# end def


if __name__ == "__main__" :
    app.run(debug=True)
