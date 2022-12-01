from utils import file_to_lines


def solve(elfs):
    sums_kcal = sorted(
        sum([int(kcal_value) for kcal_value in elf.split(" ")]) for elf in elfs
    )
    return sum(sums_kcal[-3:])


if __name__ == "__main__":
    print(solve(file_to_lines(day=1, separate_with_empty=True)))
