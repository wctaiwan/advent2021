def get_cost(input, pos) -> int:
    cost = 0
    for i in input:
        distance = abs(i - pos)
        cost += (distance * (distance + 1)) // 2
    return cost

input = []
with open('input7.txt') as input_file:
    input = [int(x) for x in input_file.readline().strip().split(',')]

min, minpos = None, None
for i in range(max(input)):
    cost = get_cost(input, i)
    if min is None or cost < min:
        min = cost
        minpos = i
print(minpos, min)
