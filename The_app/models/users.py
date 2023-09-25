from .basemodel import BaseModel, Base
from sqlalchemy import Column, String, DateTime, Boolean, Enum as SQLAlchemyEnum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_bcrypt import Bcrypt, generate_password_hash, check_password_hash

db = SQLAlchemy()
bcrypt = Bcrypt()


class User(BaseModel, Base):
    __table__ = 'users'
    email = Column(String(255), nullable=False, unique=True)
    username = Column(String(255), nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(SQLAlchemyEnum('admin', 'user'), default='user', nullable=False)
    is_active = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=False)
    posts = relationship('Post', back_populates='author')  # Define the relationship with Post


    def __init__(self, email, username, password, *args, **kwargs):
        """
        Purpose: init user
        """
        self.email = email
        self.username = username
        self.hash_password = bcrypt.generate_password_hash(password).decode('utf-8')

        super().__init__(*args,**kwargs)



    def check_password(self, password):
        """
        Purpose: pwd checking
        """
        return bcrypt.check_password_hash(self.hash_password, password)
