#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if os.environ["HBNB_TYPE_STORAGE"] == 'db':
        __tablename__ = 'users'

        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        place = relationship("Place", backref="user", cascade="all, delete-orphan")
        review = relationship("Review", backref="user", cascade="all, delete-orphan")

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''

    def __init__(self, *args, **kwargs):
        """Initializes the object using inherited attributes"""
        super().__init__(*args, **kwargs)
