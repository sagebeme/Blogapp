from flask import render_template, Blueprint,request,url_for

core =Blueprint('core', __name__)


@core.route('/')
def index():
    """
    Purpose: 
    """
    return render_template('index.html')
# end def


@core.route('/info')
def info():
    """
    Purpose: 
    """
    return render_template('info.html')
# end def