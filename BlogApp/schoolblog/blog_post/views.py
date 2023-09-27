from flask import Blueprint, Flask, abort, flash, url_for, request, render_template,redirect
from flask_login import current_user, login_required
from schoolblog import db
from schoolblog.models import Blog
from schoolblog.blog_post.forms import BlogPostForm

blog_posts = Blueprint('blog_posts', __name__)


#Creating a Blog_post
@blog_posts.route('/create', methods=["GET","POST"])
@login_required
def create():
    """
    Purpose: creates a new post in database
    """
    form = BlogPostForm()

    if form.validate_on_submit():

        blog_post = Blog(
                    title=form.title.data,
                    text=form.text.data,
                    user_id=current_user.id,
                )
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)
# end def

#Reading a Blog_post
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    """
    Purpose: gets the blog in the database
    """
    blog_post = Blog.query.get_or_404(blog_post_id)
    return render_template('blog_post.html',title=blog_post.title,
                            date=blog_post.date,post=blog_post
    )
# end def

#Updating a Blog_post
@blog_posts.route('/<int:blog_post_id>/update', methods=['GET','POST'])
@login_required
def update(blog_post_id):
    """
    Purpose: checks blog if present then updates
    """
    blog_post = Blog.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    form = BlogPostForm()


    if form.validate_on_submit():

        blog_post.title = form.title.data
        blog_post.text = form.text.data
        db.session.commit()
        flash('Blog Post Updated')
        return redirect(url_for('blog_posts.blog_post',blog_post_id=blog_post.id))

    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text

    return render_template('create_post.html',title='Updating',form=form)

# end def

#Deleting a Blog_post
@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_post_id):
    """
    Purpose: deletes a post from the database
    """
    blog_post = Blog.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))
# end def