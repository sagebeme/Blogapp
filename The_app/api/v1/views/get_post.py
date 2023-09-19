from flask import jsonify
from db.storage import get_db_connection
from api.v1.views import app_views

@app_views.route('/get_posts/<string:topic>', methods=['GET'])
def get_post(topic):
    """
    Purpose: 
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    query = 'SELECT * FROM posts WHERE topic = ?'
    cursor.execute(query, (topic,))
    post = cursor.fetchall()
    print(post)
    if post is None:
        return jsonify({'message': "No posts with this topic"}), 400
    data = []
    for row in post:
        Dict = {}
        Dict['id'] = row[0]
        Dict['date'] = row[1]
        Dict['title'] = row[2]
        Dict['content'] = row[3]
        Dict['topic'] = row[4]
        data.append(Dict)
    
    conn.close()
    return jsonify(data), 200
# end def