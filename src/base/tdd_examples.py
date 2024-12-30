def get_email_handle(email):
    """Extract the handle/username part from an email address.

    Args:
        email (str): A valid email address (e.g., 'user@example.com')

    Returns:
        str: The handle/username part before the @ symbol

    Raises:
        TypeError: If email is not a string
        ValueError: If email doesn't contain @ symbol

    Examples:
        >>> get_email_handle("user@example.com")
        'user'
        >>> get_email_handle("john.doe@company.co.uk")
        'john.doe'
    """
    pass
