import pytest
from app.logic import adjust
from app.models.input_models import MeasuredTemperature
from app.models import db_models


_MEASURE_ONE = MeasuredTemperature(
    location="foo",
    measure=10
)
_MEASURE_TWO = MeasuredTemperature(
    location="foo",
    measure=1
)
_MEASURE_THREE = MeasuredTemperature(
    location="bar",
    measure=10
)


@pytest.mark.parametrize('measures, expected', [
    # In test_curd.py we set the value of "foo.measure.temp" to 8. 10 > 8
    ([_MEASURE_ONE], [dict(location="foo", measure=8)]),
    ([_MEASURE_TWO], [dict(location="foo", measure=1)]),
    ([_MEASURE_THREE], [
        dict(location="foo", measure=1), dict(location="bar", measure=10)
    ])
])
def test_adjust_temperature(test_db, measures, expected):
    """
    GIVEN a relational database
    WHEN a list of measures is given
    IF the measures are 'hotter' than the value in DB
        THEN nothing happens
    ELIF the measures are 'cooler' than the value in DB
        THEN update the value in DB
    ELIF the location doesn't exist in DB
        THEN create location in DB and add measure value
    """
    response = adjust.adjust_temperature(measures, test_db)
    assert response == expected
