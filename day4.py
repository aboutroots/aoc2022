from utils import file_to_lines
from functools import reduce


def is_overlapping(result, row):
    x1, y1, x2, y2 = (int(v) for v in row.strip().replace("-", ",").split(","))
    # overlapping = x1<=x2 and y1 >= y2 or x2<=x1 and y2>= y1  # part 1
    overlapping = not (y1 < x2 or y2 < x1)  # part2
    return result + 1 if overlapping else result


if __name__ == "__main__":
    print(reduce(is_overlapping, file_to_lines(day=4), 0))
