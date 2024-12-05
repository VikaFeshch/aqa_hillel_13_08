import pytest
import logging
import requests




@pytest.fixture(scope='class')
def authenticate():
    auth_data = ('test_user', 'test_pass')

    response = requests.post('http://127.0.0.1:8080/auth', auth=auth_data)

    assert response.status_code == 200, f"Failed to get token: {response.text}"

    token = response.json().get('access_token')

    return {'Authorization': f'Bearer {token}'}


@pytest.mark.parametrize(
    "sort_by, limit, expected_status",
    [
        ('brand', 10, 200),
        ('price', 5, 200),
        ('year', 20, 200),
        ('brand', 50, 200),
        ('price', 30, 200),
        ('year', 10, 200),
        ('engine_volume', 0, 200),
    ]
)
def test_get_cars(sort_by, limit, expected_status, authenticate):
    url = f'http://localhost:8080/cars?sort_by={sort_by}&limit={limit}'

    # Логування запиту
    logging.info(f"Testing with sort_by={sort_by}, limit={limit}")
    logging.info(f"URL: {url}")  # Додаткове логування для перевірки правильності URL
    logging.info(f"Headers: {authenticate}")  # Логування заголовків
    # Виконання GET запиту
    response = requests.get(url, headers=authenticate)

    # Логування відповіді
    logging.info(f"Response Status Code: {response.status_code}")

    # Перевірка статусу відповіді
    assert response.status_code == expected_status
