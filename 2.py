input = []

with open('input2.txt') as input_file:
    for line in input_file:
        dir, steps = line.split(' ')
        input.append((dir, int(steps)))

x = 0
y = 0
aim = 0
for dir, steps in input:
    if dir == 'forward':
        x += steps
        y += aim * steps
    elif dir == 'up':
        aim -= steps
    else:
        aim += steps
print(x*y)