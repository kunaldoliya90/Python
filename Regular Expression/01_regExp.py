import re

def is_valid_password(password):
    """
    Check the validity of a password based on the given criteria.

    Args:
        password (str): The password to be validated.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    # Regex pattern to match the password criteria
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$")
    
    # Check if the password matches the pattern
    if pattern.match(password):
        return True
    else:
        return False

# Example usage:
password = input("Enter a password: ")

if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")
