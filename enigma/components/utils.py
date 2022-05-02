import string


def to_position(c):
    """..."""
    return ord(c) - ord("A")


def to_letter(i):
    """..."""
    return chr(i + ord("A"))


def verify_alphabet(s):
    """Checks that ``s`` contains all of the letters of the alphabet in uppercase.

    Args:
        s (list-like): the input list or string to be tested.

    Returns:
        bool: True if ok, False otherwise.

    Raises:
        ValueError: if not OK.

    """

    if len(s) == 26 and set(s) == set(string.ascii_uppercase):
        return True

    raise ValueError("Must be a unique mapping from/to all 26 letters.")
    return False
