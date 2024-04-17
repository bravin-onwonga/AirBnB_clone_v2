#!/usr/bin/python3
""" This model defines our CRUD operations on data in our db """

import os
from sqlalchmey import create_engine
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    cls_lst = [User, State, City, Amenity, Place, Review]

    tbls_dict = {
             User: 'users', State: 'states', City: 'cities',
             Amenity: 'amenities', Place: 'place', Review: 'review'
            }

    def __init__(self):
        username = os.environ["HBNB_MYSQL_USER"]
        passwd = os.environ["HBNB_MYSQL_PWD"]
        host = os.environ["HBNB_MYSQL_HOST"]
        dbName = os.environ["HBNB_MYSQL_DB"]
        env = os.environ["HBNB_ENV"]

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                           (username, passwd, host, dbName), pool_pre_ping=True)

        if (env == "test"):
            tables = self.__engine.tablenames()

            for table in tables:
                table.drop(self.__engine)

    def all(self, cls=None):
        my_dict = {}
        if (cls):
            objs = self.__session.query(cls).all()

            for obj in objs:
                key = cls.__name__ + '.' + obj.id
                value = obj.__dict__
                my_dict.update({key: value})
        else:
            for item in self.cls_lst:
                query = self.__session.query(item).all()

                for obj in objs:
                    key = cls.__name__ + '.' + obj.id
                    value = obj.__dict__
                    my_dict.update({key: value})

        return (my_dict)

    def new(self, obj):
        my_dict = obj.to_dict()
        self.__session.add_all([obj.__cls__(my_dict)])

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if (obj):
            key = obj.__class__ + '.' + obj.id
            cls_name = obj.__class__
            obj_del = self.__session.query(cls_name).filter(cls_name.id == key)

    def reload(self):
        pass
