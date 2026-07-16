from src.auth import login_with_email


def test_login_with_email_returns_true_for_valid_credentials():
    users = {"user@example.com": "password123"}

    assert login_with_email("user@example.com", "password123", users) is True


def test_login_with_email_returns_false_for_invalid_email():
    users = {"user@example.com": "password123"}

    assert login_with_email("missing@example.com", "password123", users) is False


def test_login_with_email_returns_false_for_invalid_password():
    users = {"user@example.com": "password123"}

    assert login_with_email("user@example.com", "wrongpassword", users) is False
