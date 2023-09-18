from flask import Blueprint, jsonify, request
from db.storage import get_db_connection
from api.v1.views import app_views
from datetime import datetime

@app_views.route('/get_posts/<string:topic>', methods=['GET'])
def get_posts(topic):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM posts WHERE topic = ?"
    cursor.execute(query, (topic,))
    post = cursor.fetchone()
    data = {
        'id': post[0],
        'title': post[1],
        'content': post[2],
        'author': post[3],
        'date': post[4],
        'topic': post[5]
    }
    conn.close()
    return jsonify(data)
