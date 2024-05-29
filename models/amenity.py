#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    if models.my_env == "db":
        __tablename__ = "amenities"

        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place', secondary=place_amenity, back_populates='amenities')

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates an instance"""
        super().__init__(*args, **kwargs)
