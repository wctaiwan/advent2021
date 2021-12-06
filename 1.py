input = []

with open('input1.txt') as input_file:
    for line in input_file:
        input.append(int(line))

increases = 0
previous = input[0] + input[1] + input[2]
for windowStart in range(1, len(input)-2):
    current = previous - input[windowStart-1] + input[windowStart + 2]
    if current > previous:
        increases += 1
    previous = current

print(increases)