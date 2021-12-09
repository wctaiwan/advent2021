grid = []
with open('input9.txt') as input_file:
    for line in input_file:
        if line == '\n':
            break
        grid.append([int(x) for x in line.strip()])

rows = len(grid)
cols = len(grid[0])
basins = {}
for i in range(rows):
    for j in range(cols):
        if (j == 0 or grid[i][j-1] > grid[i][j]) and \
                (j == cols - 1 or grid[i][j+1] > grid[i][j]) and \
                (i == 0 or grid[i-1][j] > grid[i][j]) and \
                (i == rows - 1 or grid[i+1][j] > grid[i][j]):
            basins[(i, j)] = None

for lowest_point in basins:
    visited = set()
    frontier = {lowest_point}
    while len(frontier) > 0:
        new_frontier = set()
        for i, j in frontier:
            if j > 0 and grid[i][j-1] > grid[i][j] and grid[i][j-1] < 9 and (i, j-1) not in visited:
                new_frontier.add((i, j-1))
            if j < cols-1 and grid[i][j+1] > grid[i][j] and grid[i][j+1] < 9 and (i, j+1) not in visited:
                new_frontier.add((i, j+1))
            if i > 0 and grid[i-1][j] > grid[i][j] and grid[i-1][j] < 9 and (i-1, j) not in visited:
                new_frontier.add((i-1, j))
            if i < rows-1 and grid[i+1][j] > grid[i][j] and grid[i+1][j] < 9 and (i+1, j) not in visited:
                new_frontier.add((i+1, j))
            visited.add((i, j))
        frontier = new_frontier
    basins[lowest_point] = len(visited)

largest_3 = sorted(basins.values(), key=lambda x: -x)[:3]
print(largest_3[0] * largest_3[1] * largest_3[2])
