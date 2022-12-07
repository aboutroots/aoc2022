from utils import file_to_lines


def solve(signal):
    for window_start in range(len(signal)):
        window_end = window_start + 14
        window = signal[window_start:window_end]
        if len(set(window)) == len(window):
            return window_end


if __name__ == "__main__":
    print(solve(file_to_lines(day=6)[0].strip()))
