from typing import List, Set, Callable

from utils import file_to_lines
from functools import reduce


def get_priority(x: str) -> int:
    return ord(x) - 96 if x.islower() else ord(x) - 38


def find_duplicate(sets: List[Set]) -> str:
    return reduce(lambda a, b: a.intersection(b), sets).pop()


def get_sets_first(rows: List[str]) -> List[Set]:
    for backpack in [list(row.strip()) for row in rows]:
        half = len(backpack) // 2
        yield [set(backpack[:half]), set(backpack[half:])]


def get_sets_second(rows: List[str]) -> List[Set]:
    n_chunks = 3
    for i in range(0, len(rows), n_chunks):
        yield [set(row.strip()) for row in rows[i: i + n_chunks]]


def solve(rows: List[str], sets_generator: Callable):
    result = 0
    for sets in sets_generator(rows):
        duplicate = find_duplicate(sets)
        result += get_priority(duplicate)
    return result


if __name__ == "__main__":
    rows = file_to_lines(day=3)
    print(solve(rows=rows, sets_generator=get_sets_first))
    print(solve(rows=rows, sets_generator=get_sets_second))
