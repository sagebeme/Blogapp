from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Email
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed

from flask_login import current_user
from schoolblog.models import User

class LoginForm(FlaskForm):
    """Login form

    Args:
        FlaskForm (_type_): creates flask forms
    """
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    """user registration form

    Args:
        FlaskForm (_type_): creates flask forms

    Raises:
        ValidationError: email in db
        ValidationError: user in db
    """
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password',
                             validators=[DataRequired(),
                                         EqualTo('pass_confirm',
                                                 message='Passwords must match!!!')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        """
        Purpose: checks if email is used
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has already been registered')

    def check_username(self, field):
        """
        Purpose: checks if username is used
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has already been registered')


class UpdateUserForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update!')

    def check_email(self, field):
        """
        Purpose: checks if email is used
        """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has already been registered')

    def check_username(self, field):
        """
        Purpose: checks if username is used
        """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has already been registered')

