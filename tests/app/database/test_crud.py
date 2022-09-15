import pytest
# from sqlalchemy.exc import PendingRollbackError
from app.database import crud, schemas
from app.models import db_models

_SAMPLE_MEASURE = db_models.Measure(
    id=1, temperature=10, location_id=1
)
_SAMPLE_LOCATION = db_models.Location(
    id=1, name="foo", measure=_SAMPLE_MEASURE
)

@pytest.mark.parametrize("location, expected", [
    ("foo", _SAMPLE_LOCATION),
    # int are automatically converted to str, so we use type dict as input
    (dict(test="foo"), None)
])
def test_create_location(test_db, location, expected):
    """
    GIVEN a relational database
    WHEN a new location is being created
    IF the values are of the expected types
        THEN the new location is created and returned
    ELSE an AtributeError is returned
    """
    if expected:
        response = crud.create_location(test_db, location)
        assert response.id == expected.id
        assert response.name == expected.name

    else:
        with pytest.raises(Exception):
            crud.create_location(test_db, location)

        # Cancel the changes for the wrong input:
        test_db.rollback()


@pytest.mark.parametrize("location, temp, expected", [
    (1, 10, _SAMPLE_MEASURE),
    # int are automatically converted to str, so we use type dict as input
    (1, dict(test="foo"), None),
    (dict(test="foo"), 10, None)
])
def test_create_location_measure(test_db, location, temp, expected):
    """
    GIVEN a relational database
    WHEN a new measure is being created
    IF the values are of the expected types
        THEN the new measure is created and returned
    ELSE an AtributeError is returned
    """
    if expected:
        response = crud.create_location_measure(test_db, temp, location)
        assert response.id == expected.id
        assert response.temperature == expected.temperature
        assert response.location_id == expected.location_id

    else:
        with pytest.raises(Exception):
            crud.create_location_measure(test_db, temp, location)

        # Cancel the changes for the wrong input:
        test_db.rollback()


@pytest.mark.parametrize("location_id, expected", [
    (1, _SAMPLE_LOCATION),
    (2, None),  # doesn't exist
    ("foo", None),  # Id is not of type int

])
def test_get_location(test_db, location_id, expected):
    """
    """
    response = crud.get_location(test_db, location_id)

    if response:
        assert response.name == expected.name
        assert response.id == expected.id
        assert response.measure.temperature == expected.measure.temperature

    else:
        assert response == expected
