#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Review(Base, BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True,  nullable=False)
    content = Column(String(60),  nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'),  nullable=False)