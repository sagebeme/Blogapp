"""
Main application entry point.

This module initializes the Flask app and runs it.
"""

from flask import Flask, render_template, url_for
from api.v1.views import app_views
from db.storage import init_user, init_post


app = Flask(__name__)


# Register blueprints for API versions
app.register_blueprint(app_views, url_prefix='/api/v1')

init_user()
init_post()


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


if __name__ == '__main__':
    app.run(debug=True)
