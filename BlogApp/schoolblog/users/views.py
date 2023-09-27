from flask import Blueprint, flash, render_template, redirect, request, url_for
from flask_login import login_user, current_user, logout_user, login_required

from schoolblog.models import User, Blog
from schoolblog import db
from schoolblog.users.user_form import RegistrationForm, LoginForm, UpdateUserForm
from schoolblog.users.pictute_handler import add_pic


users = Blueprint('users', __name__)

#register user
@users.route('/register', methods=['GET', 'POST'])
def register():
    """
    Purpose: register a user
    """
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)

# end def


#login user
@users.route('/login', methods=['GET','POST'])
def login():
    """
    Purpose: login user
    """
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash("login Success")

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html', form=form)
# end def


#logout user
@users.route("/logout")
def logout():
    """
    Purpose: log out user
    """
    logout_user()
    return redirect(url_for("core.index"))


# user acc(update user form)
@users.route('/account',methods=['GET','POST'])
@login_required
def account():
    """
    Purpose: gets user data and updates it
    """

    form = UpdateUserForm()
    if form.validate_on_submit():

        if form.picture.data:
            username = current_user.username
            pic = add_pic(form.picture.data,username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated!')
        return redirect(url_for('users.account'))

    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email

    profile_image = url_for('static',filename='profile_pics/'+current_user.profile_image)
    return render_template('account.html',profile_image=profile_image,form=form)


# end def

@users.route("/<username>")
def user_posts(username):
    """
    Purpose: gets data form the data base
    """
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = Blog.query.filter_by(author=user).order_by(Blog.date.desc()).paginate(page=page, per_page=7)
    return render_template('user_blog_post.html', blog_posts=blog_posts, user=user)
# end def