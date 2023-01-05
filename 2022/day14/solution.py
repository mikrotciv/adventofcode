"""Day 14: Regolith Reservoir"""

from pathlib import Path
from typing import Tuple

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

class Grid():
    def __init__(self):
        self.grid = []
        self.offset = 0 # Starting 'x' offset
        self.sand_col = 500

    def load_from_file(self, filename: str, corrected_scan: bool=False):
        """Creates grid from file"""
        self.grid.clear()

        parsed_input = []
        min_x = None
        max_x = None
        max_y = None

        # Get min/max for x,y to create grid
        with open(filename, 'r', encoding='utf-8') as input_file:
            # Convert input to int and find out min/max for both x,y
            for line in input_file:
                temp = []
                for coordinate in line.strip().split("->"):
                    pair = coordinate.split(',')
                    x = int(pair[0])
                    y = int(pair[1])
                    if min_x is None or min_x > x:
                        min_x = x
                    if max_x is None or max_x < x:
                        max_x = x
                    if max_y is None or max_y < y:
                        max_y = y
                    temp.append((x,y))
                parsed_input.append(temp)
        self.offset = min_x

        # Create grid
        if corrected_scan:
            max_y += 2
            self.offset = self.sand_col - max_y
            self.grid = [['.' for _ in range(2*max_y + 1)] for _ in range(max_y)]
            self.grid.append(['#' for _ in range(2*max_y + 1)])
        else:
            self.grid = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y+1)]

        # Populate grid
        for line in parsed_input:
            for idx in range(1, len(line)):
                self._draw_line(line[idx-1], line[idx])

    def _draw_line(self, start: Tuple[int], end: Tuple[int]):
        """Draws a line inside the grid based on two points"""
        start_x, start_y = start
        end_x, end_y = end

        x_increment = 1 if start_x <= end_x else -1
        y_increment = 1 if start_y <= end_y else -1
        for row in range(start_y, end_y+y_increment, y_increment):
            for col in range(start_x - self.offset, end_x - self.offset + x_increment, x_increment):
                self.grid[row][col] = "#"

    def print_grid(self):
        """Prints grid"""
        for char in str(self.offset):
            print(f"{char : >3}")
        for idx, line in enumerate(self.grid):
            print(idx, f"{''.join(line)}")

    @property
    def max_row(self) -> int:
        """Returns max number of rows in grid"""
        return len(self.grid)

    @property
    def max_col(self) -> int:
        """Returns max number of columns in grid"""
        return len(self.grid[0])

def get_sand_count(grid: Grid) -> int:
    """Returns number of sand at rest before overflowing"""
    get_sand_count.count = 0

    def dfs(row: int, col: int):
        # Check out of bounds and stop sand flow
        if row < 0 or col < 0 or \
            row >= grid.max_row or col >= grid.max_col:
            return False
        # Check if point is fillable w/ sand
        if grid.grid[row][col] in ("#", "o"):
            return True

        # Set sand while we are within boundary
        if dfs(row+1, col) and \
           dfs(row+1, col-1) and \
           dfs(row+1, col+1):
            grid.grid[row][col] = "o"
            get_sand_count.count += 1
            return True
        return False

    dfs(0, grid.sand_col-grid.offset)
    return get_sand_count.count

def main():
    """Print solution"""
    grid = Grid()
    grid.load_from_file(INPUT_FILE)
    print(f"Part 1: {get_sand_count(grid)}")

    grid.load_from_file(INPUT_FILE, corrected_scan=True)
    print(f"Part 2: {get_sand_count(grid)}")

if __name__ == '__main__':
    main()
