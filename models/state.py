#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    if models.my_env == "db":
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        city = relationship("City", backref="states")

    else:
        """ State class """
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter method for cities"""
            my_lst = []
            curr_cities = models.storage.all(City)
            for city in curr_cities.values():
                if city.state_id == self.id:
                    my_lst.append(city)
            return my_lst
