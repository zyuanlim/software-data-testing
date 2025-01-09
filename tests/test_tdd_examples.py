import pytest

from src.base.tdd_examples import get_email_handle


# Phase 1: Basic functionality
def test_basic_email():
    assert get_email_handle("user@example.com") == "user"


# Phase 2: Handle plus sign notation
def test_email_with_plus():
    assert get_email_handle("user+tag@example.com") == "user"
    assert get_email_handle("john.doe+newsletter@example.com") == "john.doe"


# Phase 3: Format validation
@pytest.mark.parametrize(
    "invalid_email,error_message",
    [
        ("invalid-email", "Must contain exactly one @"),
        ("user@company@example.com", "Must contain exactly one @"),
        ("@example.com", "Username cannot be empty"),
        ("", "Email cannot be empty"),
    ],
)
def test_invalid_formats(invalid_email, error_message):
    with pytest.raises(ValueError, match=error_message):
        get_email_handle(invalid_email)


# Phase 4: Type validation
@pytest.mark.parametrize(
    "invalid_input",
    [None, 123, [], {}],
)
def test_invalid_types(invalid_input):
    with pytest.raises(TypeError, match="Email must be a string"):
        get_email_handle(invalid_input)
