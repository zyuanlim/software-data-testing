import pytest

from src.base.tdd_examples import get_email_handle


@pytest.mark.parametrize(
    "email,expected",
    [
        ("user@example.com", "user"),
        ("john.doe@company.co.uk", "john.doe"),
        ("test_123@test.org", "test_123"),
        ("simple@test.com", "simple"),
    ],
)
def test_get_email_handle(email, expected):
    assert get_email_handle(email) == expected


@pytest.mark.parametrize(
    "invalid_email",
    [
        "invalid-email",
        "user@company@example.com",
    ],
)
def test_invalid_email(invalid_email):
    with pytest.raises(ValueError):
        get_email_handle(invalid_email)


def test_invalid_type():
    with pytest.raises(TypeError):
        get_email_handle(123)
