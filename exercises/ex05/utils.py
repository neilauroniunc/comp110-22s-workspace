"""Functions and stuff."""

__author__ = '730449902'


def only_evens(int_list: list[int]) -> list[int]:
    """Returns only even items from a list."""
    return_list: list[int] = []
    for num in int_list:
        if num % 2 == 0:
            return_list.append(num)
    return return_list


def sub(int_list: list[int], start_ind: int, end_ind: int) -> list[int]:
    """Slices a list via given indices."""
    return_list: list[int] = []
    if start_ind < 0:
        start_ind = 0
    if end_ind > len(int_list) - 1:
        end_ind = len(int_list)
    if len(int_list) == 0 or start_ind > len(int_list) - 1 or end_ind <= 0:
        return []
    end_ind -= 1
    while start_ind <= end_ind:
        return_list.append(int_list[start_ind])
        start_ind += 1
    return return_list
        

def concat(int_list_1: list[int], int_list_2: list[int]) -> list[int]:
    """Concatenates two lists."""
    final_list = int_list_1
    for item in int_list_2:
        final_list.append(item)
    return final_list