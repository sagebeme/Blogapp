from flask import Blueprint, jsonify, request, session, redirect, url_for
from db.storage import get_db_connection
from api.v1.views import app_views

@app_views.route('/login_view', methods=['POST'])
def login_view():
    session['logged-in'] = True
    return redirect(url_for('posts'))
