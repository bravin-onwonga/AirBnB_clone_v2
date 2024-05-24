#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    if models.my_env == 'db':
        __tablename__ = "places"

        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        review = relationship("Review", backref="place", cascade="all, delete-orphan")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    if models.my_env != 'db':
        @property
        def reviews(self):
            """Getter method for all reviews linked to a place"""
            from models import storage
            reviews_lst = []

            my_dict = storage.all(Review)

            for value in my_dict.items():
                if value.get('place_id') == self.id:
                    reviews_lst.append(value)

            return reviews_lst


    def __init__(self, *args, **kwargs):
        """Insantiates instance by calling parent class"""
        super().__init__(*args, **kwargs)
