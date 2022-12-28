"""Day 11: Monkey in the Middle"""

from collections import deque
from pathlib import Path
from typing import Dict, List

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

class Monkey():
    """Monkey containing items and operations it performs"""
    common_divisor = 1
    def __init__(self):
        self.items = None
        self.operation = None
        self.optimized_operation = None
        self.divisible = None
        self.true_monkey = None
        self.false_monkey = None
        self.inspect_count = 0

    def play(self, optimized:bool=False):
        """Sequence of events monkey does for each item"""
        while self.items:
            item = self.items.popleft()
            worry_level = self.inspect(item, optimized)
            self.throw(worry_level, optimized)

    def receive(self, item: int) -> None:
        """Receives items from another monkey"""
        self.items.append(item)

    def inspect(self, item: int, optimized:bool=False) -> List[int]:
        """Inspect item and returns new worry level"""
        self.inspect_count += 1
        return self.optimized_operation(item, self.common_divisor) if optimized else self.operation(item)

    def throw(self, item: int, optimized:bool=False) -> None:
        """Throws item to other monkey after decreasing worry level"""
        new_worry_level = item if optimized else item // 3
        target_monkey = self.false_monkey if new_worry_level % self.divisible else self.true_monkey
        target_monkey.receive(new_worry_level)

def parse_input() -> Dict[int, Monkey]:
    """Parse input file and return starting state of collection of monkeys"""
    monkeys = {}
    with open(INPUT_FILE, 'r', encoding="utf-8") as input_file:
        current_monkey = Monkey()
        for line in input_file:
            match line := line.strip().split(":"):
                case ["Starting items", *starting_items]:
                    current_monkey.items = deque([int(item.strip()) for item in starting_items[0].strip().split(',')])
                case ["Operation", *operation]:
                    expression = operation[0].split('=')[1]
                    match expression := expression.strip().split():
                        case ["old", "+", *operand]:
                            operand = operand[0]
                            if operand == "old":
                                current_monkey.optimized_operation = \
                                    lambda old, divisor: ((old % divisor) * 2) % divisor
                                current_monkey.operation = lambda old: old *2
                            else:
                                current_monkey.optimized_operation = \
                                    lambda old, divisor, operand=int(operand): ((old % divisor) + (operand % divisor)) % divisor
                                current_monkey.operation = \
                                    lambda old, operand=int(operand): old + operand
                        case ["old", "*", *operand]:
                            operand = operand[0]
                            if operand == "old":
                                current_monkey.optimized_operation = \
                                    lambda old, divisor: ((old % divisor) * (old % divisor)) % divisor
                                current_monkey.operation = lambda old: old * old
                            else:
                                current_monkey.optimized_operation = \
                                    lambda old, divisor, operand=int(operand): ((old % divisor) * (operand % divisor)) % divisor
                                current_monkey.operation = \
                                    lambda old, operand=int(operand): old * operand
                        case _:
                            raise ValueError(f"Unsupported expression: {expression}")
                case ["Test", *test]:
                    current_monkey.divisible = int(test[0].split()[-1])
                    Monkey.common_divisor *= current_monkey.divisible
                case ["If true", *true_monkey]:
                    monkey_id = int(true_monkey[0].split()[-1])
                    target_monkey = monkeys.get(monkey_id)
                    if target_monkey is None:
                        target_monkey = Monkey()
                        monkeys[monkey_id] = target_monkey
                    current_monkey.true_monkey = target_monkey
                case ["If false", *false_monkey]:
                    monkey_id = int(false_monkey[0].split()[-1])
                    target_monkey = monkeys.get(monkey_id)
                    if target_monkey is None:
                        target_monkey = Monkey()
                        monkeys[monkey_id] = target_monkey
                    current_monkey.false_monkey = target_monkey
                case [""]:
                    pass
                case _:
                    _, monkey_id = line[0].split()
                    monkey_id = int(monkey_id)
                    current_monkey = monkeys.get(monkey_id, Monkey())
                    monkeys[monkey_id] = current_monkey
    return monkeys

def compute_monkey_business(monkeys: Dict[int, Monkey], rounds: int, optimized:bool=False):
    """Returns the product of top two inspect count"""
    for _ in range(rounds):
        for monkey_id in range(len(monkeys)): #pylint: disable=consider-using-enumerate
            monkey = monkeys[monkey_id]
            monkey.play(optimized=optimized)
    inspect_counts = sorted([monkey.inspect_count for monkey in monkeys.values()])
    return inspect_counts[-1] * inspect_counts[-2]

def main():
    """Print solution"""
    monkeys = parse_input()
    print(f"Part 1: {compute_monkey_business(monkeys, 20)}")
    monkeys = parse_input()
    print(f"Part 2: {compute_monkey_business(monkeys, 10000, optimized=True)}")

if __name__ == '__main__':
    main()
