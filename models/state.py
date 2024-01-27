#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import os
STORAGE_TYPE = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        if STORAGE_TYPE != 'db':
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if city[0] == 'City':
                    lista.append(var[key])
            for elem in lista:
                if elem.state_id == self.id:
                    result.append(elem)
            return result
        else:
            return [city for city in self.cities]
