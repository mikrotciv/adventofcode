"""Day 13: Distress Signal"""
from ast import literal_eval
from pathlib import Path
from typing import List, Union

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

def parse_input():
    """Parses input and returns a list of pairs"""

def compare(left: List, right: List) -> Union[bool, None]:
    """Compares left and right list to see if they are in correct order"""
    left_size = len(left)
    right_size = len(right)
    for idx in range(min(left_size, right_size)):
        left_current = left[idx]
        right_current = right[idx]
        left_list = isinstance(left_current, list)
        right_list = isinstance(right_current, list)
        if left_list or right_list:
            result = compare(
                left_current if left_list else [left_current],
                right_current if right_list else [right_current]
            )
            if result is None:
                continue
            return result
        if left_current == right_current:
            continue
        return left_current < right_current
    if left_size == right_size:
        return None
    return left_size < right_size

def sum_of_correct_order():
    """Returns the sum of packet index in correct order"""
    correct_index: List[int] = []
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        count = 0
        while left := input_file.readline():
            left = left.strip()
            if not left:
                continue
            right = input_file.readline().strip()
            count += 1
            if compare(literal_eval(left), literal_eval(right)):
                correct_index.append(count)
    return sum(correct_index)

def sorted_insert(value: List, sorted_list: List) -> int:
    """Inserts value into sorted list and returns the index"""
    start = 0
    end = len(sorted_list)
    while start < end:
        mid = start + (end-start)//2
        if compare(value, sorted_list[mid]):
            end = mid
        else:
            start = mid + 1
    sorted_list.insert(start, value)
    return start

def get_decoder_key():
    """Returns the decoder key by extracting positions of [[2]] and [[6]] in sorted packet list"""
    sorted_list = []
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            if line == "\n":
                continue
            parsed_line = literal_eval(line.strip())
            sorted_insert(parsed_line, sorted_list)
    divider_2 = sorted_insert([[2]], sorted_list) + 1
    divider_6 = sorted_insert([[6]], sorted_list) + 1
    return divider_2 * divider_6

def main():
    """Print solution"""
    print(f"Part 1: {sum_of_correct_order()}")
    print(f"Part 2: {get_decoder_key()}")

if __name__ == '__main__':
    main()
