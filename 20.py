from typing import List

lookup = []

def expand(grid: List[str], fill: str) -> List[str]:
    cols = len(grid[0])
    results = []
    results.append(''.join([fill for _ in range(cols+2)]))
    for row in grid:
        results.append(fill + row + fill)
    results.append(''.join([fill for _ in range(cols+2)]))
    return results

def prev_value(row: int, col: int, grid: List[str], fill: str) -> str:
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return fill
    return grid[row][col]

def lookup_next(binary: str) -> str:
    index = 0
    pos = len(binary) - 1
    while pos >= 0:
        if binary[pos] == '#':
            index += 2 ** (len(binary) - 1 - pos)
        pos -= 1
    return lookup[index]

def get_next(row: int, col: int, grid: List[str], fill: str) -> str:
    binary = ''
    for i in [row-1, row, row+1]:
        for j in [col-1, col, col+1]:
            binary += prev_value(i, j, grid, fill)
    return lookup_next(binary)

def count_lit(grid: List[str]) -> int:
    result = 0
    for row in grid:
        result += sum([1 if x == '#' else 0 for x in row])
    return result

grid = []
with open('input20.txt') as input_file:
    lookup = input_file.readline().strip()
    input_file.readline()
    line = input_file.readline().strip()
    while line != '':
        grid.append(line)
        line = input_file.readline().strip()

iter = 1
while iter <= 50:
    if iter % 2 == 1:
        fill = '.'
    else:
        fill = '#'
    grid = expand(grid, fill)
    next_grid = []
    for row in range(len(grid)):
        next_row = ''
        for col in range(len(grid[0])):
            next_row += get_next(row, col, grid, fill)
        next_grid.append(next_row)
    grid = next_grid
    iter += 1

print(count_lit(grid))
