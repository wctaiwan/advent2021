input = []
with open('input6.txt') as input_file:
    input = [int(x) for x in input_file.readline().strip().split(',')]

prev = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

for fish in input:
    prev[fish] += 1

for i in range(256):
    cur = {}
    for j in range(8):
        cur[j] = prev[j+1]
    cur[8] = prev[0]
    cur[6] += prev[0]
    prev = cur

print(sum(cur.values()))