from schoolblog.models import Blog
from flask import render_template, Blueprint,request,url_for

core =Blueprint('core', __name__)


@core.route('/')
def index():
    """
    Purpose: 
    """
    page = request.args.get('page', 1, type=int)
    blog_post = Blog.query.order_by(Blog.date.desc()).paginate(page=page,per_page=7)

    return render_template('index.html', blog_post=blog_post)
# end def


@core.route('/info')
def info():
    """
    Purpose: 
    """
    return render_template('info.html')
# end def