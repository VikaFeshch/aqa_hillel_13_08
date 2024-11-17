import pytest
import logging
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = 'http://127.0.0.1:8080'


@pytest.fixture(scope='class')
def authenticated_session():
    session = requests.Session()
    auth_data = HTTPBasicAuth('test_user', 'test_pass')
    url = f'{BASE_URL}/auth'
    response = session.post(url, auth=auth_data)
    assert response.status_code == 200, f"Failed to get token: {response.text}"
    token = response.json().get('access_token')
    session.headers.update({'Authorization': f'Bearer {token}'})
    return session


@pytest.mark.parametrize(
    "sort_by, limit, expected_status",
    [
        ('brand', 10, 200),
        ('price', 5, 200),
        ('year', 20, 200),
        ('brand', 50, 200),
        ('price', 30, 200),
        ('year', 10, 200),
        ('year', 0, 400),
        ('name', 10, 422),
        ('engine_volume', 5, 200),
    ]
)
def test_get_cars(sort_by, limit, expected_status, authenticated_session):
    url = f'{BASE_URL}/cars?sort_by={sort_by}&limit={limit}'
    logging.info(f"Testing with sort_by={sort_by}, limit={limit}")
    response = authenticated_session.get(url)
    print(f"Response Data: {response.json()}")
    logging.info(f"Response Status Code: {response.status_code}")
    assert response.status_code == expected_status
    if response.status_code == 200:
        assert len(response.json()) <= limit, "Received more items than allowed by the limit"
    if response.status_code == 200:
        data = response.json()
        if limit > 0:
            assert len(data) <= limit, f"Received more items than limit: {limit}"

        for car in data:
            assert 'brand' in car, "Missing 'brand' field in car data"
            assert 'year' in car, "Missing 'year' field in car data"
            assert 'engine_volume' in car, "Missing 'engine_volume' field in car data"
            assert 'price' in car, "Missing 'price' field in car data"

    elif response.status_code == 400:
        error_message = response.json().get('message', '')
        assert "limit must be greater than zero" in error_message.lower(), "Unexpected error message"

    elif response.status_code == 422:
        error_message = response.json().get('message', '')
        assert error_message, f"Invalid sort field: {sort_by}"

