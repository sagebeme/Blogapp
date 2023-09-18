"""
Module for handling API endpoints related to blog posts.

This module provides routes and views for creating, updating, deleting, and displaying posts.
"""

from flask import Blueprint, jsonify, request
from db.storage import get_db_connection
from api.v1.views import app_views
from datetime import datetime

#posts_bp = Blueprint('posts', __name__)

@app_views.route('/add', methods=['POST'])
def add_post():
    conn = get_db_connection()
    cursor = conn.cursor()

    title = request.form.get('title')
    content = request.form.get('content')
    topic = request.form.get('topic')
    #author = request.form.get('author')
    author = 'Dennis'
    date = datetime.now().date()
    year = datetime.now().year
    date_posted = str(date) + '/' + str(year)

    cursor.execute('''
        INSERT INTO posts (title, content, author, date_posted, topic)
        VALUES (?, ?, ?, ?, ?)
    ''', (title, content, author, date_posted, topic))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Post added successfully'})
