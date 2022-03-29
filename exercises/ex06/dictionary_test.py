"""Testing dictionary functions."""

__author__ = '730449902'

from dictionary import invert, favorite_color, count
import pytest


with pytest.raises(KeyError):
    """Tests that duplicate values results in a KeyError."""
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_empty_dict() -> None:
    """Tests if inverting an empty dict returns and empty dict."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_normal() -> None:
    """Tests the regular inverting of the function."""
    test_dict: dict[str, str] = {'apple': 'cat'}
    assert invert(test_dict) == {'cat': 'apple'}


def test_favorite_color_equal_colors() -> None:
    """Ensures function returns the first color if two colors appear equally."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "brown", "Kris": "blue", "Ria": "blue", "Neil": "brown"}
    assert favorite_color(test_dict) == 'brown'


def test_favorite_color_empty_dict() -> None:
    """Tests that the function returns an empty string for an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ''


def test_favorite_color_normal() -> None:
    """Tests the normal use of the function."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "brown", "Kris": "blue", "Ria": "blue"}
    assert favorite_color(test_dict) == 'blue'


def test_count_empty_list() -> None:
    """Tests that an empty list returns an empty dict."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_normal() -> None:
    """Tests normal function use."""
    test_list: list[str] = ['poo', 'poo', 'poo', 'pee']
    assert count(test_list) == {'poo': 3, 'pee': 1}


def test_count_another_normal() -> None:
    """Tests another normal function use."""
    test_list: list[str] = ['dog', 'cat', 'raptureiscoming', 'pee', 'dog']
    assert count(test_list) == {'dog': 2, 'cat': 1, 'raptureiscoming': 1, 'pee': 1}
