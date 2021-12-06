input = []

with open('input5.txt') as input_file:
    for line in input_file:
        if input == '\n':
            break
        parts = line.strip().split(' -> ')
        x1, y1 = parts[0].split(',')
        x2, y2 = parts[1].split(',')
        input.append(((int(x1), int(y1)), (int(x2), int(y2))))

grid = []
for i in range(1000):
    grid.append([0 for _ in range(1000)])

for line in input:
    (x1, y1), (x2, y2) = line
    if x1 != x2 and y1 != y2:
        continue
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2+1):
            grid[x1][y] += 1
    else:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2+1):
            grid[x][y1] += 1

for line in input:
    (x1, y1), (x2, y2) = line
    if x1 == x2 or y1 == y2:
        continue
    x_step = 1 if x2 > x1 else -1
    y_step = 1 if y2 > y1 else -1
    x, y = x1, y1
    while x != x2:
        grid[x][y] +=1
        x += x_step
        y += y_step
    grid[x][y] += 1

points = 0
for i in range(1000):
    for j in range(1000):
        if grid[i][j] > 1:
            points += 1
print(points)