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

