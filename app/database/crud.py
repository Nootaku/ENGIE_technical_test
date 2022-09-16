"""CRUD UTILS

This file contains reusable function to interact with the data in the database.
"""

from sqlalchemy.orm import Session
from app.models import db_models as models
from . import schemas


def get_location(db: Session, location_id: int):
    """Query DB and return location based on given location id."""
    return db.query(models.Location).filter(
        models.Location.id == location_id).first()


def get_location_by_name(db: Session, name: str):
    """Query DB and return location based on given location name."""
    return db.query(models.Location).filter(
        models.Location.name == name).first()


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    """Return all Locations present in DB."""
    return db.query(models.Location).offset(skip).limit(limit).all()


def create_location(db: Session, location_name: str):
    """Add new location to DB and return created location."""
    db_location = models.Location(name=location_name)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


# def get_meaures(db: Session, skip: int = 0, limit: int = 100):
#     """Return all Measures present in DB."""
#     return db.query(models.Measure).offset(skip).limit(limit).all()


def create_location_measure(
    db: Session,
    measure: int,
    location_id: int
):
    """Add new measure to DB and return created location."""
    db_measure = models.Measure(
        temperature=measure,
        location_id=location_id
    )
    db.add(db_measure)
    db.commit()
    db.refresh(db_measure)
    return db_measure


def update_measure_by_id(
    db: Session,
    measure: schemas.Measure,
    new_measure: int
):
    """Update measure temperature by ID."""
    assert isinstance(new_measure, int)
    db_measure = db.query(models.Measure).filter(
        models.Measure.id == measure.id)
    db_measure.update({"temperature": new_measure}, synchronize_session=False)
    db.commit()
