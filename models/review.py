#!/usr/bin/python3
""" Review module for the HBNB project """
import models
from sqlalchemy import Column, String, ForeignKey
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """ Review classto store review information """
    if models.my_env == "db":
        __tablename__ = "reviews"

        place_id = Column(String(1024), nullable=False)
        user_id = Column(String(60), ForeignKey("places.id"), nullable=False)
        text = Column(String(60), ForeignKey("users.id"), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        """Instantiates an instance by calling the parent class"""
        super().__init__(*args, **kwargs)
