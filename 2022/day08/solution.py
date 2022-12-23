"""Day 8: Treetop Tree House"""

from pathlib import Path
from typing import List

INPUT_FILE = Path(Path(__file__).parent, "input.txt")

def parse_input() -> List[List[int]]:
    """Parses input file and returns a grid of tree heights"""
    grid: List[List[int]] = []
    with open(INPUT_FILE, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            grid.append([int(height) for height in line.strip()])
    return grid

def count_visible_trees(grid: List[List[int]]) -> int:
    """Returns the number of visible trees from outside the gride"""
    row_size = len(grid)
    # Assuming we have at least one row and all rows have same number of columns
    col_size = len(grid[0])

    total = 2 * row_size + 2 * (col_size - 2) # Perimeter is always visisble
    for row in range(1,row_size-1):
        for col in range(1,col_size-1):
            # Evaluate if visible by checking (x,y) > max of its row/col
            current = grid[row][col]
            max_up = max(grid[x][col] for x in range(0, row))
            max_down = max(grid[x][col] for x in range(row+1, row_size))
            max_left = max(grid[row][y] for y in range(0, col))
            max_right = max(grid[row][y] for y in range(col+1, col_size))
            if current > max_up or current > max_down or current > max_left or current > max_right:
                total += 1

    return total

def get_highest_scenic_score(grid: List[List[int]]) -> int:
    """Returns the highest scenic score within the grid"""
    row_size = len(grid)
    # Assuming we have at least one row and all rows have same number of columns
    col_size = len(grid[0])

    def get_view_distance(height: int, trees: List[int]) -> int:
        """Returns the viewing distance a single direction"""
        distance = 0
        for tree_height in trees:
            distance += 1
            if tree_height >= height:
                break
        return distance

    max_score = 0
    for row in range(1,row_size-1):
        for col in range(1,col_size-1):
            current = grid[row][col]
            view_up = get_view_distance(current, [grid[x][col] for x in range(row-1, -1, -1)])
            view_down = get_view_distance(current, [grid[x][col] for x in range(row+1, row_size)])
            view_left = get_view_distance(current, [grid[row][y] for y in range(col-1, -1, -1)])
            view_right = get_view_distance(current, [grid[row][y] for y in range(col+1, col_size)])
            score = view_up * view_down * view_left * view_right
            if score > max_score:
                max_score = score
    return max_score

def main():
    """Print solutions"""
    grid = parse_input()
    print(f"Part 1: {count_visible_trees(grid)}")
    print(f"Part 2: {get_highest_scenic_score(grid)}")

if __name__ == '__main__':
    main()
