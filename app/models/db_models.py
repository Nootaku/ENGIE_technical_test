"""SQLALCHEMY MODELS

This file contains the SQLAlchemy model classes. They inherit from the Base
class (see /app/database/database.py).

Documentation:
https://docs.sqlalchemy.org/en/14/orm/quickstart.html
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    # Define linkages between two mapped classes
    measure = relationship("Measure", back_populates="location", uselist=False)


class Measure(Base):
    __tablename__ = "measures"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Integer)
    location_id = Column(Integer, ForeignKey("locations.id"))

    # Define linkages between two mapped classes
    location = relationship("Location", back_populates="measure")
