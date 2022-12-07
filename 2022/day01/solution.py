#!/usr/bin/env python

from collections import deque

INPUT = "input.txt"

def get_max_calories():
    """Calculates the max number of calories Elf is carrying"""
    max_calories = 0
    with open(INPUT, 'r') as f:
        elf_calories = 0
        for line in f:
            if line == "\n":
                max_calories = max(max_calories, elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(line)
    return max_calories

def top_n_calories_sum(n: int):
    """Calculates the sum of top n calories"""
    top_calories = deque([0]*n)
    with open(INPUT, 'r') as f:
        elf_calories = 0
        for line in f:
            if line == "\n":
                for idx, calories in enumerate(top_calories):
                    if elf_calories > calories:
                        top_calories.insert(idx, elf_calories)
                        while len(top_calories) > n:
                            top_calories.pop()
                        break
                elf_calories = 0
            else:
                try:
                    elf_calories += int(line)
                except ValueError as ex:
                    print(f"Failed to convert {line} to integer: {ex}")
                except:
                    print(f"Failed to convert {line} to integer")

    return sum(top_calories)

def main():
    """Print solutions"""
    print(f"Elf carrying max calories: {get_max_calories()}")
    print(f"Sum of top three calories: {top_n_calories_sum(3)}")

if __name__ == '__main__':
    main()
