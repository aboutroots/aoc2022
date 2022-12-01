from utils import file_to_lines


def solve(elfs):
    sums_kcal = set(sum([int(val) for val in elf.split(' ')]) for elf in elfs)
    total = 0
    for n in range(3):
        elf = max(sums_kcal)
        total += elf
        sums_kcal.discard(elf)
    return total


if __name__ == "__main__":
    print(solve(file_to_lines(day=1, separate_with_empty=True)))
