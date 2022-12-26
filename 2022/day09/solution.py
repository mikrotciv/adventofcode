"""Day 9: Rope Bridge"""

from pathlib import Path
from types import MappingProxyType
from typing import List, Tuple

DIRECTION_MAP = MappingProxyType({
    # Axis, Step
    "U": (1,1),
    "D": (1,-1),
    "L": (0,-1),
    "R": (0,1)
})

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

Instruction = Tuple[str, int]
def parse_input() -> List[Instruction]:
    """Parses input and returns a list of instructions"""
    instructions = []
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            instructions.append((line[0], int(line[1:])))
    return instructions

def move_tail(head: List[int], tail: List[int]) -> bool:
    """Updates tail position if necessary"""
    x_diff = head[0] - tail[0]
    y_diff = head[1] - tail[1]
    if abs(x_diff) > 1 or abs(y_diff) > 1:
        if x_diff == 0: # Same x-axis
            tail[1] += 1 if y_diff > 0 else -1
        elif y_diff == 0: # Same y-axis
            tail[0] += 1 if x_diff > 0 else -1
        else: # Move diagonal
            tail[0] += 1 if x_diff > 0 else -1
            tail[1] += 1 if y_diff > 0 else -1
        return True
    return False

def total_tail_visit(instructions: List[Instruction]) -> int:
    """Returns unique number of positions visited by tail"""
    # Setup
    head = [0,0]
    tail = [0,0]
    visited = {tuple(tail)}
    for instruction in instructions:
        direction, count = instruction
        axis, step = DIRECTION_MAP[direction]
        for _ in range(count):
            head[axis] += step
            if move_tail(head, tail):
                visited.add(tuple(tail))
    return len(visited)

def total_nth_tail_visit(instructions: List[Instruction], length: int) -> int:
    """Returns unique number of positions visited by tail"""
    # Setup
    if length < 2:
        raise ValueError("Length must be at least 2")
    rope = [[0,0] for _ in range(length)]
    visited = {tuple(rope[-1])}

    for instruction in instructions:
        direction, count = instruction
        axis, step = DIRECTION_MAP[direction]
        for _ in range(count):
            # Update head
            rope[0][axis] += step
            # Update rest of the rope
            for idx in range(1,len(rope)):
                move_tail(rope[idx-1], rope[idx])
            # Keep track of tail
            visited.add(tuple(rope[-1]))
    return len(visited)

def main():
    """Print solution"""
    instructions = parse_input()
    print(f"Part 1: {total_tail_visit(instructions)}")
    print(f"Part 2: {total_nth_tail_visit(instructions, 10)}")

if __name__ == '__main__':
    main()
