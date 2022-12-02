from typing import List


def read_int_list(filename: str = 'input.txt') -> List[int]:
    with open(filename) as read_file:
        data = [int(x.strip()) for x in read_file.readlines()]
    return data


def read_int_matrix(filename: str = 'input.txt') -> List[List[int]]:
    with open(filename) as read_file:
        data = [[int(y) for y in x.strip().split(' ')] for x in read_file.readlines()]
    return data


def read_str_list(filename: str = 'input.txt') -> List[str]:
    with open(filename) as read_file:
        data = [x.strip() for x in read_file.readlines()]
    return data


def read_str_matrix(filename: str = 'input.txt') -> List[List[str]]:
    with open(filename) as read_file:
        data = [[y for y in x.strip().split(' ')] for x in read_file.readlines()]
    return data
