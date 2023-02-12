from re import sub


def split_camel_case(string: str):
    """

    Args:
        string: String to split.

    Returns:
        str: Camel case string split out with spaces in between words.

    """
    return sub(r"(?!^)([A-Z0-9][a-z]*)", r" \1", string)
