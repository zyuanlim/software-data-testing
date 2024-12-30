def get_email_handle(email):
    """Extract the handle/username part from an email address.

    This function demonstrates TDD with progressively complex requirements:
    1. Basic email handle extraction
    2. Handle dots in username
    3. Handle plus sign notation (removes everything after +)
    4. Format validation
    5. Type checking

    Args:
        email (str): A valid email address (e.g., 'user@example.com', 'user+tag@example.com')

    Returns:
        str: The handle/username part before the @ symbol
             - Keeps dots (.)
             - Removes everything after plus (+) if present

    Raises:
        TypeError: If email is not a string
        ValueError: If email format is invalid, with specific messages:
            - "Email cannot be empty"
            - "Must contain exactly one @"
            - "Username cannot be empty"

    Examples:
        >>> get_email_handle("user@example.com")
        'user'
        >>> get_email_handle("john.doe+newsletter@example.com")
        'john.doe'
    """
    pass
