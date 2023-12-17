#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    @property
    def cities(self):
        '''getter attribute cities that returns the list of City instances'''
        from models import storage
        cities = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                cities.append(city)
        return cities