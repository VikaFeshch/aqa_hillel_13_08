import os
import logging
import pytest

from lesson_11.src.homework_11 import log_event

LOG_FILE = 'login_system.log'


def read_log_file():
    """
    Function for read from file
    """
    with open(LOG_FILE, 'r') as file:
        content_of_file = file.read()
        # print(f"{LOG_FILE} {str(a)}")
        return content_of_file


def test_log_event_success():
    username = "user1"
    status = "success"

    log_event(username, status)
    content_of_file = read_log_file()

    assert f"Login event - Username: {username}, Status: {status}" in content_of_file


def test_log_event_expired():
    username = "user2"
    status = "expired"

    log_event(username, status)
    content_of_file = read_log_file()

    assert "Login event - Username: user2, Status: expired" in content_of_file


def test_log_event_failed():
    username = "user3"
    status = "failed"

    log_event(username, status)
    content_of_file = read_log_file()

    assert "Login event - Username: user3, Status: failed" in content_of_file
