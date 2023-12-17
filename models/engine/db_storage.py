#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        '''initializes the database engine'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''returns a dictionary of all objects
        Returns:
            returns a dictionary of all objects
        '''
        classes = [State, City, User, Place, Review, Amenity]
        new_dict = {}
        if cls is None:
            for cls in classes:
                for obj in self.__session.query(cls):
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        else:
            if type(cls) is str:
                cls = eval(cls)
            for obj in self.__session.query(cls).all():
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        ''' adds the object to the current database session'''
        self.__session.add(obj)
        
    def save(self):
        ''' commits all changes of the current database session'''
        self.__session.commit()
    
    def delete(self, obj=None):
        '''deletes from the current database session obj if not None'''
        if obj is not None:
            self.__session.delete(obj)
    
    def reload(self):
        '''create all tables in the database and create the current database session'''
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
