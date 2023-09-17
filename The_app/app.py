"""
Main application entry point.

This module initializes the Flask app and runs it.
"""

from flask import Flask, render_template
from api.v1.views import app_views
from db import init_db

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
