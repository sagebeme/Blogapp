"""
Module for handling API endpoints related to blog posts.

This module provides routes and views for creating, updating, deleting, and displaying posts.
"""

from flask import Blueprint, jsonify, request, redirect, url_for
from db.storage import get_db_connection
from api.v1.views import app_views
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

#posts_bp = Blueprint('posts', __name__)

@app_views.route('/register', methods=['POST'])
def add_user():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    confirm_password = request.form.get('password')  # You might want to generate this automatically

    if password != confirm_password:
        return redirect(url_for('login'))

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    password = hashed_password

    conn = get_db_connection()
    cursor = conn.cursor()


    cursor.execute('''
        INSERT INTO user (email, username, password, password)
        VALUES (?, ?, ?, ?)
    ''', (email,username, password, hashed_password))

    conn.commit()
    conn.close()
    return redirect (url_for('login'))


