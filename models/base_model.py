#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
import os
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import datetime

Base = declarative_base()

storage_type = os.environ["HBNB_TYPE_STORAGE"]


class BaseModel:
    """A base class for all hbnb models"""

    if storage_type == "db":
        id = Column(String(60), primary_key=True, unique=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        if (my_dict.get('_sa_instance_state')):
            my_dict.pop('_sa_instance_state')
        return my_dict

    def delete(self):
        """ Calls the storage method delete"""
        from models import storage
        storage.delete(self)
