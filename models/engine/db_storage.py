#!/usr/bin/python3
""" This model defines our CRUD operations on data in our db """

import os
from sqlalchemy import MetaData, create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Class for database storage"""
    __engine = None
    __session = None

    cls_lst = [User, State, City, Amenity, Place, Review]

    def __init__(self):
        """Initializes the class"""
        username = os.environ["HBNB_MYSQL_USER"]
        passwd = os.environ["HBNB_MYSQL_PWD"]
        host = os.environ["HBNB_MYSQL_HOST"]
        dbName = os.environ["HBNB_MYSQL_DB"]

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, passwd, host, dbName), pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            metadata = MetaData()
            metadata.reflect(bind=self.__engine)
            for table in reversed(metadata.sorted_tables):
                table.drop(self.__engine)


    def all(self, cls=None):
        """Creates a list all the objects based on classes passed"""
        my_dict = {}
        if (cls):
            objs = self.__session.query(cls).all()

            for obj in objs:
                key = cls.__name__ + '.' + obj.id
                value = obj
                my_dict.update({key: value})
        else:
            for item in self.cls_lst:
                objs = self.__session.query(item).all()
                cls = item

                for obj in objs:
                    key = cls.__name__ + '.' + obj.id
                    value = obj
                    my_dict.update({key: value})

        return (my_dict)

    def new(self, obj):
        """Adds a new obj to a current storage"""
        self.__session.add(obj)

    def save(self):
        """Commit all our transaction to the DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an obj if it is passed as an arg"""
        if (obj):
            key = obj.__class__ + '.' + obj.id
            cls_name = obj.__class__
            obj_del = self.__session.query(cls_name).filter(cls_name.id == key)
            if (obj_del):
                self.__session.delete(obj_del)

    def reload(self):
        """Established our session"""
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Calls remove on session"""
        if self.__session:
            self.__session.close()
        else:
            Session.close()
        self.reload()
