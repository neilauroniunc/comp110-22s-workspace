"""Function tests."""

__author__ = '730449902'

from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests only_evens with an empty list."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_no_evens() -> None:
    """Tests only_evens with no evens."""
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []


def test_only_evens_many_evens() -> None:
    """Tests only_evens with many evens."""
    test_list: list[int] = [1, 2, 4, 6, 7]
    assert only_evens(test_list) == [2, 4, 6]


def test_sub_empty() -> None:
    """Tests sub with empty list."""
    test_list: list[int] = []
    assert sub(test_list, 1, 2) == []


def test_sub_extreme_indices() -> None:
    """Tests sub with indices beyond the range of the given list."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(test_list, -3, 43) == [1, 2, 3, 4, 5]


def test_sub_normal_slice() -> None:
    """Tests sub with normal indices and a normal list."""
    test_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(test_list, -1, 5) == [1, 2, 3, 4, 5]


def test_concat_empty_lists() -> None:
    """Tests concat with empty lists."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_normal_lists() -> None:
    """Tests concat with normal lists."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6]


def test_concat_different_sized_lists() -> None:
    """Tests concat with different sized lists."""
    list_1: list[int] = [1, 2, 3]
    list_2: list[int] = [4, 5, 6, 7, 8, 9]
    assert concat(list_1, list_2) == [1, 2, 3, 4, 5, 6, 7, 8, 9]