"""
Module for handling API endpoints related to blog posts.

This module provides routes and views for creating, updating, deleting, and displaying posts.
"""

from flask import Blueprint, jsonify, request
from db.storage import get_db_connection
from api.v1.views import app_views

#posts_bp = Blueprint('posts', __name__)

@app_views.route('/add', methods=['POST'])
def add_post():
    conn = get_db_connection()
    cursor = conn.cursor()

    topic = request.form.get('topic')
    title = request.form.get('title')
    content = request.form.get('content')

    date_posted = request.form.get('date_posted')  # You might want to generate this automatically

    cursor.execute('''
        INSERT INTO posts (topic, title, content, date)
        VALUES (?, ?, ?, ?)
    ''', (topic,title, content, date_posted))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Post added successfully'})
