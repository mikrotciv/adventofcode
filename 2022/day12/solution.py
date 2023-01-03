
"""Day 12: Hill Climbing Algorithm"""

from collections import deque
from pathlib import Path
from typing import List, Tuple

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

class Grid():
    def __init__(self):
        self.grid = []
        self.start = None

    @property
    def max_row(self) -> int:
        """Returns number of rows in grid"""
        return len(self.grid)

    @property
    def max_col(self) -> int:
        """Returns number of columns in grid"""
        return len(self.grid[0])

    def load_from_file(self, filename: str):
        """Creates grid from file"""
        self.grid.clear()
        with open(filename, 'r', encoding='utf-8') as input_file:
            row = 0
            for line in input_file:
                temp = []
                for col, char in enumerate(line.strip()):
                    if char == "S":
                        self.start = (row, col)
                    temp.append(char)
                self.grid.append(temp)
                row += 1

    def get_neighbors(self, row: int, col: int) -> List[Tuple[int]]:
        """Returns a list of neighbors for current point"""
        neighbors = []
        if row + 1 < self.max_row:
            neighbors.append((row+1, col))
        if row - 1 >= 0:
            neighbors.append((row-1, col))
        if col + 1 < self.max_col:
            neighbors.append((row, col+1))
        if col - 1 >= 0:
            neighbors.append((row, col-1))
        return neighbors

    def get_point(self, row: int, col: int) -> str:
        """Returns value at grid"""
        return self.grid[row][col]

def get_elevation(char: str) -> int:
    """
    Returns elevation value
    For 'S' and 'E', it will return values for 'a' and 'z' respectively
    """
    return ord({'S': 'a', 'E': 'z'}.get(char, char))


def find_shortest_path_from_start(start: List[int], grid: Grid) -> int:
    """Finds the shortest path from start to end"""
    count = 0
    dq = deque([start])
    visited = set()
    found = False
    while dq and not found:
        size = len(dq)
        for _ in range(size):
            position = tuple(dq.popleft())
            row, col = position
            if position in visited:
                continue
            visited.add(position)
            current = grid.get_point(row, col)
            if current == "E":
                found = True
                break

            neighbors = grid.get_neighbors(row, col)
            for neighbor in neighbors:
                if tuple(neighbor) in visited:
                    continue
                next_row, next_col = neighbor
                value = grid.get_point(next_row, next_col)

                if (get_elevation(value) - get_elevation(current)) > 1:
                    continue

                dq.append(neighbor)
        if not found:
            count += 1
    return count if found else 0

def find_shortest_path(grid: Grid) -> int:
    """Finds the shortest path from any 'a' level to end"""
    min_path = None
    for row in range(grid.max_row):
        for col in range(grid.max_col):
            current = grid.get_point(row, col)
            if current == "a":
                path = find_shortest_path_from_start([row, col], grid)
                if path and (min_path is None or min_path > path):
                    min_path = path
    return min_path

def main():
    """Print solution"""
    grid = Grid()
    grid.load_from_file(INPUT_FILE)

    print(f"Part 1: {find_shortest_path_from_start(grid.start, grid)}")
    print(f"Part 2: {find_shortest_path(grid)}")

if __name__ == '__main__':
    main()
