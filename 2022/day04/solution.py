#!/usr/bin/env python
"""Day 4: Camp Cleanup"""

from pathlib import Path
from typing import List

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

def is_contained(first_range: List[str], second_range: List[str]) -> bool:
    """Checks if one pair is fully contained in other pair"""
    first_x = int(first_range[0])
    first_y = int(first_range[1])
    second_x = int(second_range[0])
    second_y = int(second_range[1])
    return (first_x <= second_x and first_y >= second_y) \
        or (second_x <= first_x and second_y >= first_y)

def get_total_contained() -> int:
    """Returns the total number of pairs that are fully contained"""
    total = 0
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            first, second = line.strip().split(',')
            first_range = first.split('-')
            second_range = second.split('-')
            if is_contained(first_range, second_range):
                total += 1
    return total

def is_overlapped(first_range: List[str], second_range: List[str]) -> bool:
    """Returns if two pairs are overlapped"""
    first_x = int(first_range[0])
    first_y = int(first_range[1])
    second_x = int(second_range[0])
    second_y = int(second_range[1])

    return not(first_y < second_x or second_y < first_x)

def get_total_overlapped() -> int:
    """Returns the total number of overlapped sections"""
    total = 0
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            first, second = line.strip().split(',')
            first_range = first.split('-')
            second_range = second.split('-')
            if is_overlapped(first_range, second_range):
                total += 1
    return total

def main() -> None:
    """Print solutions"""
    print(f"Total contained: {get_total_contained()}")
    print(f"Total overlapped: {get_total_overlapped()}")

if __name__ == '__main__':
    main()
