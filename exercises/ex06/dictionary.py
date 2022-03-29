"""Dictionary functions!"""

__author__ = '730449902'


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts key-value pairs in a dictionary of strings."""
    return_dict: dict[str, str] = {}
    for key in a:
        if a[key] in return_dict:
            raise KeyError('Duplicate key in dictionary')
        else:
            return_dict[a[key]] = key
    return return_dict


def favorite_color(a: dict[str, str]) -> str:
    """Returns most chosen color from a dictionary of favorite colors."""
    color_dict: dict[str, int] = {}
    for key in a:
        if a[key] in color_dict:
            color_dict[a[key]] += 1
        else:
            color_dict[a[key]] = 1
    dummy_max: int = 0
    final_max: int = 0
    max_color: str = ''
    for key in color_dict:
        dummy_max = color_dict[key]
        if dummy_max > final_max:
            final_max = dummy_max
            max_color = key
    return max_color


def count(a: list[str]) -> dict[str, int]:
    """Creates dictionary that counts the number of times a string occurs in a list."""
    count_dict: dict[str, int] = {}
    for item in a:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict