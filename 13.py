points = set()
instructions = []

with open('input13.txt') as input_file:
    line = input_file.readline().strip()
    while line != '':
        x, y = line.split(',')
        points.add((int(x), int(y)))
        line = input_file.readline().strip()

    line = input_file.readline().strip()
    while line != '':
        axis, val = line[len('fold along '):].split('=')
        instructions.append((axis, int(val)))
        line = input_file.readline().strip()

for axis, val in instructions:
    for x, y in points.copy():
        if axis == 'x' and x > val:
            points.remove((x, y))
            points.add((val*2- x, y))
        if axis == 'y' and y > val:
            points.remove((x, y))
            points.add((x, val*2 - y))

max_x = max([x for (x, _) in points])
max_y = max([y for (_, y) in points])
for row in range(max_y + 1):
    row_chars = []
    for col in range(max_x + 1):
        if (col, row) in points:
            row_chars.append('#')
        else:
            row_chars.append(' ')
    print(''.join(row_chars))
