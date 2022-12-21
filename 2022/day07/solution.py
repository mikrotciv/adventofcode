"""Day 7: No Space Left On Device"""

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

MAX_SIZE = 100000
MIN_FREE_SIZE = 30000000
TOTAL_SIZE = 70000000

@dataclass
class File():
    """File and directory are considered same object
    Difference between them are:
    File:
    - Has valid size
    - Has no children
    Directory:
    - Has invalid size (0)
    - Has children
    """
    size: int
    name: str
    children: Dict
    parent: None

def construct_filesystem() -> File:
    """Parses input file to create the filesystem"""
    head = File(0, "", {}, None)
    current = head
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        while line := input_file.readline().split():
            if line[0] == "$": # Command
                command = line[1]
                if command == "cd":
                    name = line[2]
                    if name == "..":
                        current = current.parent
                    else:
                        child = File(0, name, {}, current)
                        current.children[name] = child
                        current = child
                elif command == "ls":
                    continue
                else:
                    raise ValueError(f"Unsupported command: {command}")
            else: # Output
                name = line[1]
                child = File(
                    0 if line[0] == "dir" else int(line[0]),
                    name, {}, current
                )
                current.children[name] = child
    return head

def get_total_sum_at_most_max(root: File) -> int:
    """Returns the sum of all directories with total size of at most MAX_SIZE"""
    valid_dir:List[int] = []

    def dfs(root: File) -> int:
        if len(root.children) == 0:
            return root.size
        total = 0
        for child in root.children.values():
            total += dfs(child)
        if total <= MAX_SIZE:
            valid_dir.append(total)
        return total

    dfs(root)
    return sum(valid_dir)

def get_min_dir_size_to_free(root: File):
    """Returns the minimum directory size to free"""
    dir_size:List[int] = []

    def dfs(root: File) -> int:
        if len(root.children) == 0:
            return root.size
        total = 0
        for child in root.children.values():
            total += dfs(child)
        dir_size.append(total)
        return total
    root_size = dfs(root)
    current_free = TOTAL_SIZE - root_size
    target_free = MIN_FREE_SIZE - current_free
    result = root_size

    # Binary search to find min size to free
    dir_size = sorted(dir_size)
    start = 0
    end = len(dir_size) - 1
    while start < end:
        mid = start + (end-start)//2
        if dir_size[mid] < target_free:
            start = mid +1
        else:
            if dir_size[mid] < result:
                result = dir_size[mid]
            end = mid
    return result

def main():
    """Prints solution"""
    head = construct_filesystem()
    print(f"Part 1: {get_total_sum_at_most_max(head.children['/'])}")
    print(f"Part 2: {get_min_dir_size_to_free(head.children['/'])}")

if __name__ == '__main__':
    main()
