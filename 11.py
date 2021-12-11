from typing import List

SIZE = 10

def flash(grid: List[List[int]], i: int, j: int) -> None:
    pts = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
    for p, q in pts:
        if p >= 0 and p < SIZE and q >= 0 and q < SIZE and grid[p][q] >= 0:
            grid[p][q] += 1
    grid[i][j] = -1

grid = []
with open('input11.txt') as input_file:
    for line in input_file:
        if line == '\n':
            break
        row = [int(x) for x in line.strip()]
        grid.append(row)

all_flashing = False
iter = 0
while not all_flashing:
    iter += 1
    for i in range(SIZE):
        for j in range(SIZE):
            grid[i][j] += 1
    has_new_flashes = True
    while has_new_flashes:
        has_new_flashes = False
        for i in range(SIZE):
            for j in range(SIZE):
                if grid[i][j] >= SIZE:
                    flash(grid, i, j)
                    has_new_flashes = True
    total = sum([sum(row) for row in grid])
    if (total == -1 * SIZE * SIZE):
        all_flashing = True
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] < 0:
                grid[i][j] = 0

print(iter)
