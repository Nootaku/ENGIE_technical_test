"""ITEM SCHEMAS

This file contains the schemas used when creating and/or reading data.

Each schema is composed of three layers:
    1. ItemBase: a Pydantic BaseModel
    2. CreateItem: inherits from the ItemBase, and adds args for item creation
       (this is currently unused but could be important in the future)
    3. Item: inherits from the ItemBase and adds args for item reading

Note:
    The 'orm_mode' is used to tell Pydantic that the item is not a dict but an
    ORM model.
"""
from pydantic import BaseModel


class MeasureBase(BaseModel):
    temperature: float


class MeasureCreate(MeasureBase):
    pass


class Measure(MeasureBase):
    id: int
    location_id: int

    class Config:
        orm_mode = True


class LocationBase(BaseModel):
    name: str


class LocationCreate(LocationBase):
    pass


class Location(LocationBase):
    id: int
    measure: Measure | None = None

    class Config:
        orm_mode = True
