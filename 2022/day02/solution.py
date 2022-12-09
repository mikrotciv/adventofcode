#!/usr/bin/env python
"""Day 2: Rock Paper Scissors"""

from enum import Enum
from types import MappingProxyType
from typing import Mapping, Union

INPUT_FILE = "input.txt"

class Moves(Enum):
    """Points associated with each move"""
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Outcome(Enum):
    """Points associated with each outcome"""
    LOST = 0
    DRAW = 3
    WIN = 6

RESULT_MATRIX = (
    (Outcome.DRAW, Outcome.WIN, Outcome.LOST),
    (Outcome.LOST, Outcome.DRAW, Outcome.WIN),
    (Outcome.WIN, Outcome.LOST, Outcome.DRAW),
)

def evaluate(op_move: Moves, my_move: Moves) -> int:
    """Evaluates total points for round"""
    diff = op_move.value - my_move.value
    if diff == 0:
        return Outcome.DRAW.value + my_move.value
    elif diff in (-1, 2):
        return Outcome.WIN.value + my_move.value
    elif diff in (1, -2):
        return Outcome.LOST.value + my_move.value
    else:
        raise Exception("Invalid outcome")

def calculate_total_score(key: Mapping[str, Moves]) -> int:
    """Calculates the total score according to the strategy guide"""
    total_score = 0
    with open(INPUT_FILE, "r") as input_file:
        for line in input_file:
            op_move, my_move = line.split()
            total_score += evaluate(key[op_move], key[my_move])
    return total_score

def corrected_total_score(key: Mapping[str, Union[Moves, Outcome]]) -> int:
    """Calculates the correct total score"""
    total_score = 0
    with open(INPUT_FILE, "r") as input_file:
        for line in input_file:
            op_move, result = line.split()
            outcomes = RESULT_MATRIX[key[op_move].value - 1]
            expected = key[result]
            for idx, outcome in enumerate(outcomes):
                if expected == outcome:
                    total_score += (expected.value + idx + 1)
    return total_score

def main():
    """Prints the solution"""
    # Part 1
    guess_key = MappingProxyType({
        "A": Moves.ROCK,
        "B": Moves.PAPER,
        "C": Moves.SCISSORS,
        "X": Moves.ROCK,
        "Y": Moves.PAPER,
        "Z": Moves.SCISSORS
    })
    print(f"Total score: {calculate_total_score(guess_key)}")

    # Part 2
    correct_key = MappingProxyType({
        "A": Moves.ROCK,
        "B": Moves.PAPER,
        "C": Moves.SCISSORS,
        "X": Outcome.LOST,
        "Y": Outcome.DRAW,
        "Z": Outcome.WIN
    })
    print(f"Corrected total score: {corrected_total_score(correct_key)}")

if __name__ == "__main__":
    main()
