"""Dictionary related utility functions."""

__author__ = "730449902"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read rows of csv into 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, 'r', encoding='utf8')
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform row-orientated table to column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Returns num_rows rows from the top of a given table."""
    return_dict: dict[str, list[str]] = {}
    if num_rows >= len(table):
        return table
    else:
        for col in table:
            n_list: list[str] = []
            iterator: int = 0
            while iterator < num_rows:
                n_list.append(table[col][iterator])
                iterator += 1
            return_dict[col] = n_list
        return return_dict


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Select specific columns from a dictionary."""
    return_dict: dict[str, list[str]] = {}
    for col in names:
        return_dict[col] = table[col]
    return return_dict


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatanate two different tables into one."""
    return_dict: dict[str, list[str]] = {}
    for col in table_1:
        return_dict[col] = table_1[col]
    for col in table_2:
        if col in return_dict:
            return_dict[col] = return_dict[col] + table_2[col]
        else:
            return_dict[col] = table_2[col]
    return return_dict


def count(val_list: list[str]) -> dict[str, int]:
    """Count instances of items in a list."""
    return_dict: dict[str, int] = {}
    for item in val_list:
        if item in return_dict:
            return_dict[item] += 1
        else:
            return_dict[item] = 1
    return return_dict