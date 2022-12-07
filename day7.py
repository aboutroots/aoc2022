from utils import file_to_lines


def get_node_from_tree(tree, path):
    elem = tree
    for val in path:
        elem = elem[val]
    return elem


def parse_dirname(row):
    return row.strip().split(" ")[-1]


def parse_filename(row):
    size, filename = row.strip().split(" ")
    return int(size), filename


def build_tree(rows):
    tree = {}
    path = []
    for row in rows[1:]:
        if row.startswith("$"):
            if row.startswith("$ cd"):
                dirname = parse_dirname(row)
                if "." in dirname:
                    path.pop()
                else:
                    path.append(dirname)
            elif row.startswith("$ ls"):
                continue
        elif "dir" in row:
            dirname = parse_dirname(row)
            get_node_from_tree(tree, path)[dirname] = {}
        else:
            size, filename = parse_filename(row)
            get_node_from_tree(tree, path)[filename] = size
    return tree


def compute_sizes(tree, memory, path):
    """
    Path is required to distinguish between dirs with the same name
    located in different branches.
    Memory is for memoization (caching).
    """
    children_size = 0
    for key, value in tree.items():
        forward_path = f"{path}/{key}"
        if not isinstance(value, dict):
            size = value
        elif forward_path in memory:
            size = memory[forward_path]
        else:
            size = compute_sizes(value, memory, forward_path)
            memory[forward_path] = size
        children_size += size
    return children_size


def solve(rows):
    tree = build_tree(rows)
    memory = {}
    total_size = compute_sizes(tree, memory, "/")
    # part 1
    print(sum([val for val in memory.values() if val <= 100000]))
    # part 2
    free_size = 70000000 - total_size
    required_size = 30000000 - free_size
    print(sorted([val for val in memory.values() if val >= required_size])[0])


if __name__ == "__main__":
    solve(file_to_lines(day=7))
