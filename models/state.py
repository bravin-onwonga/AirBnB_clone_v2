#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


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

    if models.my_env != "db":
        @property
        def cities(self):
            my_lst = []
            curr_cities = models.storage.all()
            for city in curr_cities.values():
                if city.state_id == self.id:
                    my_lst.append(city)
            return my_lst
