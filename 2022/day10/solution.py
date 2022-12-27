"""Day 10: Cathode-Ray Tube"""

from pathlib import Path
from typing import List, Optional, Tuple

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

Instruction = Tuple[str, Optional[int]]
def parse_input() -> List[Instruction]:
    """Parses input file and returns Instructions object"""
    instructions = []
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            words = line.split()
            match words[0]:
                case "addx":
                    instructions.append((words[0], int(words[1])))
                case "noop":
                    instructions.append((words[0],))
                case _:
                    raise ValueError(f"Unsupported instructions: {words[0]}")
    return instructions

def sum_of_signal_strengths(instructions: List[Instruction]) -> int:
    """Returns sum of signal strengths during 20th, 60th, 100th, 140th, 180th, and 220th cycles"""
    cycles = 0
    register_x = 1
    next_check = 20
    max_check = 220
    signals = []

    for instruction in instructions:
        name = instruction[0]
        current = register_x
        if name == "addx":
            # Check if we should record mid instruction
            if cycles <= max_check and cycles == next_check - 1:
                signals.append(next_check * current)
                next_check += 40
            register_x += instruction[1]
            cycles += 2
        elif name == "noop":
            cycles += 1
        else:
            raise ValueError(f"Unsupported instructions: {name}")
        if cycles <= max_check and next_check == cycles:
            signals.append(next_check * current)
            next_check += 40
    return sum(signals)

def render(instructions: List[Instruction]) -> None:
    """Renders image from instructions"""
    grid = [['.' for _ in range(40)] for _ in range(6)]
    cycles = 0
    register_x = 1

    def update(current):
        """Updates the grid"""
        row = cycles // 40
        col = cycles % 40
        grid[row][col] = "#" if col in list(range(current-1,current+2)) else " "

    for instruction in instructions:
        name = instruction[0]
        current = register_x
        if name == "addx":
            register_x += instruction[1]
            update(current)
            cycles += 1
            update(current)
            cycles += 1

        elif name == "noop":
            update(current)
            cycles += 1
        else:
            raise ValueError(f"Unsupported instructions: {name}")
    for line in grid:
        print(''.join(line))

def main():
    """Print solutions"""
    instructions = parse_input()
    print(f"Part 1: {sum_of_signal_strengths(instructions)}")
    print("Part 2:")
    render(instructions)

if __name__ == "__main__":
    main()
