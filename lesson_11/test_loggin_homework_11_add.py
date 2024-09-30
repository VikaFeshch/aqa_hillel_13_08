import pytest
import logging
from lesson_11.src.homework_11 import log_event


def test_log_event_success(caplog):

    username = "user1"
    status = "success"

    with caplog.at_level(logging.INFO):
        log_event(username, status)

    assert len(caplog.records) == 1  # Повинен бути лише один лог-запис
    assert caplog.records[0].levelname == "INFO"  # Логування на рівні INFO
    assert "Login event - Username: user1, Status: success" in caplog.text  # Перевірка тексту повідомлення


def test_log_event_expired(caplog):
    username = "user2"
    status = "expired"

    with caplog.at_level(logging.WARNING):
        log_event(username, status)

    assert len(caplog.records) == 1  # Один лог-запис
    assert caplog.records[0].levelname == "WARNING"  # Логування на рівні WARNING
    assert "Login event - Username: user2, Status: expired" in caplog.text  # Перевірка тексту повідомлення


def test_log_event_failed(caplog):
    username = "user3"
    status = "failed"

    with caplog.at_level(logging.ERROR):
        log_event(username, status)

    assert len(caplog.records) == 1  # Один лог-запис
    assert caplog.records[0].levelname == "ERROR"  # Логування на рівні ERROR
    assert "Login event - Username: user3, Status: failed" in caplog.text  # Перевірка тексту повідомлення

