from __future__ import annotations

class Node:
    def __init__(self, value: str, next: Node):
        self.value = value
        self.next = next

pair_counts = {}
rules = {}

with open('input14.txt') as input_file:
    template_str = input_file.readline().strip()
    for i in range(len(template_str) - 1):
        first, second = template_str[i], template_str[i+1]
        if (first, second) not in pair_counts:
            pair_counts[(first, second)] = 0
        pair_counts[(first, second)] += 1

    input_file.readline()
    line = input_file.readline().strip()
    while line != '':
        chars, insert = line.strip().split(' -> ')
        first, second = [x for x in chars]
        rules[(first, second)] = insert
        line = input_file.readline().strip()

for iter in range(40):
    new_pairs = {}
    for (first, second), count in pair_counts.items():
        insert = rules.get((first, second))
        if insert is not None:
            if (first, insert) not in new_pairs:
                new_pairs[(first, insert)] = 0
            new_pairs[(first, insert)] += count
            if (insert, second) not in new_pairs:
                new_pairs[(insert, second)] = 0
            new_pairs[(insert, second)] += count
        else:
            if (first, second) not in new_pairs:
                new_pairs[(first, second)] = 0
            new_pairs[(first, second)] += count
    pair_counts = new_pairs

counts = {}
for (first, _), count in pair_counts.items():
    if first not in counts:
        counts[first] = 0
    counts[first] += count

counts[template_str[-1]] += 1

sorted_counts = sorted(counts.values())
print(sorted_counts[-1] - sorted_counts[0])
