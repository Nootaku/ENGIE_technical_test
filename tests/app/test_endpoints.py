import pytest

_LOGIC_ = 'app.main.adjust_temperature'


def test_root(test_client):
    """
    GIVEN a FastAPI test_client
    WHEN the root of the API is called
    THEN the response status code is 200
    """
    response = test_client.get('/')
    assert response.status_code == 200


@pytest.mark.parametrize("sample_input, expected", [
    ([{"location": "Doel", "measure": 10}], 200),
    ({"location": "Doel", "measure": 10}, 422)
])
def test_adjust(test_client, mocker, sample_input, expected):
    """
    GIVEN a FastAPI test_client
    WHEN the /adjust endpoint is called
    IF the input data model corresponds to what is expected
        THEN return a status code 200
    ELSE return a status code 422

    Note: This will not test all possible Exception that can be returned.
    """
    mocker.patch(_LOGIC_, return_value=[dict(location="foo", measure=10)])
    response = test_client.post('/adjust', json=sample_input)
    assert response.status_code == expected
