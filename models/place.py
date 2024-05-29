#!/usr/bin/python3
""" Place Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity


if os.environ["HBNB_TYPE_STORAGE"] == "db":
    place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
               primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
               primary_key=True, nullable=False)
    )


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
        review = relationship(
            'Review', backref="place", cascade="all, delete-orphan")
        amenities = relationship(
            'Amenity', secondary=place_amenity,
            back_populates="place_amenities", viewonly=False)

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

    def __init__(self, *args, **kwargs):
        """Insantiates instance by calling parent class"""
        super().__init__(*args, **kwargs)

    if models.my_env != 'db':
        @property
        def reviews(self):
            """Getter method for all reviews linked to a place"""
            from models import storage
            reviews_lst = []

            my_dict = storage.all(Review)

            for review in my_dict.values():
                if review.get('place_id') == self.id:
                    reviews_lst.append(review)

            return reviews_lst

        @property
        def amenities(self):
            """Getter function for amenities"""
            from models import storage
            amenities_lst = []

            my_lst = self.amenity_ids

            my_dict = storage.all(Amenity)

            for item in my_dict.values():
                if item.id in my_lst:
                    amenities_lst.append(item)

            return amenities_lst

        @amenities.setter
        def amenities(self, obj=None):
            """setter method for amenities_ids"""
            if (obj and isinstance(obj, Amenity)):
                self.amenity_ids.append(obj.id)
