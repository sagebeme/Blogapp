from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean, Enum as SQLAlchemyEnum
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class User(BaseModel, Base):
    __table__ = 'users'
    email = Column(String(255), nullable=False, unique=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(SQLAlchemyEnum('admin', 'user'), default='user', nullable=False)
    is_active = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=False)
    posts = relationship('Post', back_populates='author')  # Define the relationship with Post



    def __init__(self, *args, **kwargs):
        """
        Purpose: init user
        """
        super().__init__(*args,**kwargs)
