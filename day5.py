from collections import defaultdict
from typing import List, Tuple, Dict

from utils import file_to_lines
import re


def get_registers(header: str) -> Dict[int, List[str]]:
    header_rows = header.split("\n")[:-2]
    dummy = "$"
    values_with_dummies = [
        list(
            row.replace("   ", dummy)
            .replace(" ", "")
            .replace("]", "")
            .replace("[", "")
        )
        for row in header_rows
    ]
    registers = defaultdict(list)
    for row in reversed(values_with_dummies):
        for index, value in enumerate(row):
            if value is not dummy:
                registers[index].append(value)
    return registers


def parse_instructions(
    instructions_raw: str
) -> List[Tuple[int, int, int]]:
    instructions = []
    for raw in instructions_raw.split("\n"):
        instruction = list(int(v) for v in re.findall(f"\d+", raw))
        instructions.append(
            (instruction[0], instruction[1] - 1, instruction[2] - 1)
        )
    return instructions


def solve(header, instructions_raw, part):
    registers = get_registers(header)
    instructions = parse_instructions(instructions_raw)
    for instr in instructions:
        values_to_be_moved = []

        for _ in range(instr[0]):
            values_to_be_moved.append(registers[instr[1]].pop())

        if part == 2:
            values_to_be_moved.reverse()

        registers[instr[2]].extend(values_to_be_moved)
    return "".join([values[-1] for values in registers.values()])


if __name__ == "__main__":
    h, i = file_to_lines(day=5, separate_with_empty=True, strip_lines=False)
    print(solve(h, i, part=1))
    print(solve(h, i, part=2))
