#!/usr/bin/env python
"""Day 3: Rucksack Reorganization"""

from pathlib import Path
from typing import List, Set

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

def get_duplicate_item(first_half:str , second_half:str) -> str:
    """Returns shared items in the compartment"""
    shared = []
    lookup = set(first_half)
    for char in second_half:
        if char in lookup:
            shared.append(char)
    return shared

def evaluate_priority(item: str) -> int:
    """Returns the priority of given item"""
    assert len(item) == 1, "Item should be a character"
    value = ord(item)
    if value >= ord('a') and value <= ord('z'):
        return value - ord('a') + 1
    elif value >= ord('A') and value <= ord('Z'):
        return value - ord('A') + 27
    else:
        raise ValueError(f"Invalid input: {item}")

def total_duplicate_priority() -> int:
    """Returns the total priority of items found in both comparments"""
    total = 0
    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            word_len = len(line)
            if word_len&1 != 0:
                raise ValueError(f"Input {line} does not contain even number of items")
            first_half, second_half = set(line[:word_len//2]), set(line[word_len//2:])
            result = get_duplicate_item(first_half, second_half)
            total += evaluate_priority(result[0])
    return total

def get_shared_item(*args):
    """Returns shared item from n compartments"""
    result = set(args[0])
    for item in args[1:]:
        shared = {char for char in item if char in result}
        result = shared
    return list(result)

def total_group_priority() -> int:
    """Returns the total group priority"""
    total = 0
    with open(INPUT_FILE, 'r') as input_file:
        group:List[str] = []
        count = 0
        for line in input_file:
            group.append(line.strip())
            count +=1
            if count%3 == 0:
                result = get_shared_item(*group)
                total += evaluate_priority(result[0])
                group.clear()
    return total

def main():
    """Print solutions"""
    # Part 1
    print(f"Total: {total_duplicate_priority()}")
    # Part 2
    print(f"Total: {total_group_priority()}")


if __name__ == '__main__':
    main()
