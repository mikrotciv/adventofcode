#!/usr/bin/env python3
"""Day 1: Trebuchet"""

from pathlib import Path

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

STR_INT = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

def _part_one_logic(line: str) -> int:
    """Parses line by looking for first and last integer"""
    # Two pointers to get first and last numbers from line
    front = 0
    back = len(line)-1
    while front <= back and not line[front].isdigit():
        front += 1
    while back >= front and not line[back].isdigit():
        back -= 1
    return int("".join((line[front], line[back])))

def _part_two_logic(line: str) -> int:
    """Parses line by looking for first and last integer/spelled out integer"""
    nums = []
    for i, char in enumerate(line):
        if char.isdigit():
            nums.append(int(char))
        else:
            for j, num in enumerate(STR_INT):
                if line[i:].startswith(num):
                    nums.append(j)
    return (nums[0])*10 + nums[-1]

def calibration_sum(input_file: str, updated_logic: bool) -> int:
    """Returns sum of calibration values extracted from input file"""
    total_sum = 0
    parsing_logic = _part_two_logic if updated_logic else _part_one_logic
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Strip new line at the end
            line = line.strip()
            total_sum += parsing_logic(line)
    return total_sum

def main():
    """Print solutions"""
    print(f"Part 1: {calibration_sum(INPUT_FILE, updated_logic=False)}")
    print(f"Part 2: {calibration_sum(INPUT_FILE, updated_logic=True)}")

if __name__ == '__main__':
    main()
