#!/usr/bin/env python
"""Day 5: Supply Stacks"""

import re

from collections import defaultdict, deque
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Deque, DefaultDict, List, Tuple

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

@dataclass
class InstructionData:
    """Instruction data"""
    count: int
    source: int
    destination: int

InputTable = DefaultDict[str, Deque[str]]
Instructions = List[InstructionData]

def parse_input() -> Tuple[InputTable, Instructions]:
    """Parses input file and returns the starting table state and list of instructions to perform"""
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        # Get initial table state
        input_table = defaultdict(deque)
        line = input_file.readline()
        while line != "\n":
            for idx in range(0,len(line),4):
                word = line[idx:idx+4]
                if word[0] == "[":
                    input_table[idx//4+1].append(word[1])
            line = input_file.readline()
        # Parse instructions
        instructions = []
        pattern = "move ([0-9]+) from ([0-9]+) to ([0-9]+)"
        try:
            while line := input_file.readline().strip():
                result = re.search(pattern, line)
                instructions.append(InstructionData(
                    int(result.group(1)),   # count
                    int(result.group(2)),   # source
                    int(result.group(3))    # destination
                ))
        except AttributeError as error:
            print(f"Command did not match pattern: {pattern}; {error}")
            return None, None
        return input_table, instructions

def get_CraterMover9000_results(table_: InputTable, instructions_: Instructions) -> str:
    """Part 1: CraterMover9000 moves stack one block at a time"""
    copy_table = deepcopy(table_)
    for instruction in instructions_:
        source = copy_table[instruction.source]
        destination = copy_table[instruction.destination]
        move = [source.popleft() for idx in range(instruction.count) if source]
        destination.extendleft(move)
    return "".join([copy_table[idx+1][0] for idx in range(len(copy_table)) if copy_table[idx+1]])    

def get_CraterMover9001_results(table_: InputTable, instructions_: Instructions) -> str:
    """Part 2: CraterMover9001 moves stack one block at a time"""
    copy_table = deepcopy(table_)
    for instruction in instructions_:
        source = copy_table[instruction.source]
        destination = copy_table[instruction.destination]
        move = [source.popleft() for idx in range(instruction.count) if source]
        move.reverse()
        destination.extendleft(move)
    return "".join([copy_table[idx+1][0] for idx in range(len(copy_table)) if copy_table[idx+1]])    

def main():
    """Prints solutions"""
    input_table, instructions = parse_input()
    print(f"Part one: {get_CraterMover9000_results(input_table, instructions)}")
    print(f"Part two: {get_CraterMover9001_results(input_table, instructions)}")

if __name__ == '__main__':
    main()
