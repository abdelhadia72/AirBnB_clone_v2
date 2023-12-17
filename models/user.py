#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel, Base):
    """This class defines a user by various attributes
    Attributes:
        email: email address
        password: password to login
        first_name: first name of user
        last_name: last name of user"""
    __tablename__ = 'users'
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
