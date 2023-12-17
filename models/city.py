#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.place import Place
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey="states.id")
