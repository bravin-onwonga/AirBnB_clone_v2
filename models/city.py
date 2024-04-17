#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from mysqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    """ The city class, contains state ID and name """
    state_id = "2"
    name = "Las Vegas"
