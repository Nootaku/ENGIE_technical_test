import pytest
from sqlalchemy.exc import InterfaceError
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
    ELSE an Exception is raised
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
    ELSE an Exception is raised
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
    (dict(test="foo"), InterfaceError("foo", 'bar', 'blah')),
])
def test_get_location(test_db, location_id, expected):
    """
    GIVEN a relational database
    WHEN a location is searched by ID
    IF the values are of the expected types
        THEN the new measure is created and returned
    ELIF the value is not of type int but of one of the base types
        THEN None is returned
    ELSE an Exception is raised
    """
    if isinstance(expected, InterfaceError):
        with pytest.raises(InterfaceError):
            crud.get_location(test_db, location_id)

    else:
        response = crud.get_location(test_db, location_id)

        if response:
            assert response.name == expected.name
            assert response.id == expected.id
            assert response.measure.temperature == expected.measure.temperature

        else:
            assert response == expected


@pytest.mark.parametrize("location_id, expected", [
    ("foo", _SAMPLE_LOCATION),
    (2, None),  # doesn't exist
    (dict(test="foo"), InterfaceError("foo", 'bar', 'blah')),
])
def test_get_location_by_name(test_db, location_id, expected):
    """
    GIVEN a relational database
    WHEN a location is searched by name
    IF the values are of the expected types
        THEN the new measure is created and returned
    ELIF the value is not of type int but of one of the base types
        THEN None is returned
    ELSE an Exception is raised
    """
    if isinstance(expected, InterfaceError):
        with pytest.raises(InterfaceError):
            crud.get_location_by_name(test_db, location_id)

    else:
        response = crud.get_location_by_name(test_db, location_id)

        if response:
            assert response.name == expected.name
            assert response.id == expected.id
            assert response.measure.temperature == expected.measure.temperature

        else:
            assert response == expected


def test_get_locations(test_db):
    """
    GIVEN a relational database
    WHEN all location are queried
    THEN a list of objects is returned
    """
    response = crud.get_locations(test_db)
    assert isinstance(response, list)


@pytest.mark.parametrize('measure, new_value, expected', [
    (_SAMPLE_MEASURE, 8, 8),
    (_SAMPLE_MEASURE, 5.0, AssertionError()),
    (_SAMPLE_MEASURE, "test", AssertionError())
])
def test_update_measure_by_id(test_db, measure, new_value, expected):
    """
    GIVEN a relational database
    WHEN a measure temparature is being updated
    THEN the value is updated
    """
    if isinstance(expected, AssertionError):
        with pytest.raises(AssertionError):
            crud.update_measure_by_id(test_db, measure, new_value)

    else:
        crud.update_measure_by_id(test_db, measure, new_value)
        location_id = measure.location_id
        response = response = crud.get_location(test_db, location_id)

        assert response.measure.temperature == expected
