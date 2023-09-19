"""
Module for handling API endpoints related to blog posts.

This module provides routes and views for creating, updating, deleting, and displaying posts.
"""

from flask import Blueprint, jsonify, request
from db.storage import get_db_connection
from api.v1.views import app_views

#posts_bp = Blueprint('posts', __name__)

@app_views.route('/login', methods=['POST'])
def login_user():
    conn = get_db_connection()
    cursor = conn.cursor()

    username = request.form.get('username')
    password = request.form.get('password')

    cursor.execute('''
        SELECT * FROM user WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()
    user_dict = {}
    user_dict["id"]= user[0]
    user_dict["email"]= user[1]
    user_dict["password"]= user[2]
    user_dict["usename"]= user[3]
    user_dict["post_id"]= user[4]

    conn.commit()
    conn.close()

    return jsonify(user_dict)


