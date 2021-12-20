from typing import Set, Tuple

grid = []
with open('input15.txt') as input_file:
    for line in input_file:
        if line == '\n':
            break
        base_row = [int(x) for x in line.strip()]
        row = []
        for iter in range(5):
            row.extend([x+iter-9 if x+iter > 9 else x+iter for x in base_row])
        grid.append(row)

base_rows = len(grid)
for iter in range(1, 5):
    for base_row in grid[:base_rows]:
        grid.append([x+iter-9 if x+iter > 9 else x+iter for x in base_row])

rows = len(grid)
cols = len(grid[0])

def h_score(node: Tuple[int, int]) -> int:
    x, y = node
    return (rows-1-y) + (cols-1-x)

def get_neighbors(node: Tuple[int, int]) -> Set[Tuple[int, int]]:
    x, y = node
    results = set()
    if x > 0:
        results.add((x-1, y))
    if x < cols-1:
        results.add((x+1, y))
    if y > 0:
        results.add((x, y-1))
    if y < rows-1:
        results.add((x, y+1))
    return results

f_score = {(0, 0): h_score((0, 0))}
g_score = {(0, 0): 0}
visited = set()
fringe = {(0, 0)}

iter = 0
while len(fringe) > 0:
    lowest_f_score = None
    cur_node = None
    for node in fringe:
        if cur_node is None or f_score[node] < lowest_f_score:
            cur_node = node
            lowest_f_score = f_score[node]
    fringe.remove(cur_node)

    if cur_node == (cols-1, rows-1):
        print(g_score[cur_node])
        break

    cur_g_score = g_score[cur_node]
    neighbors = get_neighbors(cur_node)
    for neighbor in neighbors:
        if neighbor in visited:
            continue
        x, y = neighbor
        neighbor_g_score = cur_g_score + grid[y][x]
        if neighbor not in g_score or neighbor_g_score < g_score[neighbor]:
            g_score[neighbor] = neighbor_g_score
            f_score[neighbor] = neighbor_g_score + h_score(neighbor)
        fringe.add(neighbor)
    visited.add(cur_node)
