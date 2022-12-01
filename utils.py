from typing import List


def read_int_list(filename: str = 'input.txt') -> List[int]:
    with open(filename) as read_file:
        data = [int(x.strip()) for x in read_file.readlines()]
    return data


def read_str_list(filename: str = 'input.txt') -> List[str]:
    with open(filename) as read_file:
        data = [x.strip() for x in read_file.readlines()]
    return data
