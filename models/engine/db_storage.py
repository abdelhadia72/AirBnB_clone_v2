#!/usr/bin/python3
""" new class for sqlAlchemy """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        db = getenv("HBNB_MYSQL_DB")
        passwd = getenv("HBNB_MYSQL_PWD")
        
        host = getenv("HBNB_MYSQL_HOST")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            args = self.__session.query(cls)
            for arg in args:
                key = "{}.{}".format(type(arg).__name__, arg.id)
                dic[key] = arg
        else:
            lista = [State, City, User, Place, Review, Amenity]
            for clase in lista:
                args = self.__session.query(clase)
                for arg in args:
                    key = "{}.{}".format(type(arg).__name__, arg.id)
                    dic[key] = arg
        return (dic)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configuration
        """
        Base.metadata.create_all(self.__engine)
        sec = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sec)
        self.__session = Session()

    def close(self):
        """ calls remove()
        """
        self.__session.close()