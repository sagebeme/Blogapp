"""
Module for handling API endpoints related to blog posts.

This module provides routes and views for creating, updating, deleting, and displaying posts.
"""

from flask import Blueprint, jsonify, request
from db.storage import get_db_connection
from api.v1.views import app_views
from flask_bcrypt import check_password_hash


#posts_bp = Blueprint('posts', __name__)

@app_views.route('/login', methods=['POST'])
def login_user():

    username = request.form.get('username')
    password = request.form.get('password')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM user WHERE username = ?
    ''', (username,))
    user = cursor.fetchone()

    # user_dict = {}
    # user_dict["id"]= user[0]
    # user_dict["email"]= user[1]
    # user_dict["password"]= user[2]
    # user_dict["username"]= user[3]
    # user_dict["post_id"]= user[4]

    conn.close()

    if user and check_password_hash(user['password'],password):
        user_dict = {
                        "id" : user[0],
                        "email" : user[1],
                        "password": user[2],
                        "username" : user[3],
                        "post_id" : user[4]
                        }
        return jsonify(user_dict)
    else:
        return jsonify({"message": "Invalid username or password"}), 401


