#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from mysqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    """ State class """
    name = "Naveda"
