"""
Main application entry point.

This module initializes the Flask app and runs it.
"""

from flask import Flask, render_template, redirect, url_for, session
from api.v1.views import app_views
from db import init_db

app = Flask(__name__)

app.secret_key = 'Blog_app'

init_db()

# Register blueprints for API versions
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.route('/')
def home():
    """
    Purpose: homepage
    """
    return render_template('index.html')
# end def


@app.route('/register')
def register():
    """
    Purpose: register form
    """
    return render_template('register.html')
# end def


@app.route('/login')
def login():
    """
    Purpose: login page
    """
    return render_template('login.html')
# end def

@app.route('/posts')
def posts():
    print(session)
    if session.get('logged-in') is True:
        return render_template('posts.html')
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
