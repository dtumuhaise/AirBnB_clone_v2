#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase


class State(BaseModel(Base)):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
