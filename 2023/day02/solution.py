#!/usr/bin/env python3
"""Day 2: Cube Conundrum"""

import functools
import operator
import re

from collections import defaultdict
from pathlib import Path
from typing import Dict

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

def possible_id_sum(input_file: str, color_limit: Dict) -> int:
    """Returns sum of possible game ids"""
    id_sum = 0
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            game_id, sets = line.strip().split(":")
            # Extracted game id
            game_id = int(game_id.split()[-1])
            for data in re.split(";|,", sets):
                count, color = data.split()
                if int(count) > color_limit[color]:
                    break
            else:
                id_sum += game_id
    return id_sum

def possible_id_power_sum(input_file: str) -> int:
    """Returns sum of power of possible game ids"""
    power_sum = 0
    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            min_cubes = defaultdict(int)
            game_id, sets = line.strip().split(":")
            # Extracted game id
            game_id = int(game_id.split()[-1])
            for data in re.split(";|,", sets):
                count, color = data.split()
                count = int(count)
                if min_cubes[color] < count:
                    min_cubes[color] = count
            power_sum += functools.reduce(operator.mul, min_cubes.values())
    return power_sum

def main():
    """Print solutions"""
    color_limit = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    print(f"Part 1: {possible_id_sum(INPUT_FILE, color_limit)}")
    print(f"Part 2: {possible_id_power_sum(INPUT_FILE)}")

if __name__ == '__main__':
    main()
