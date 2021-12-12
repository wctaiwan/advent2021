from typing import Dict, List

def get_paths(adjacency: Dict[str, List[str]], current: str, visited_times: Dict[str, int]) -> int:
    if current == 'end':
        return 1
    total = 0
    for next in adjacency[current]:
        if visited_times.get(next, 0) == 2:
            continue
        if next.lower() == next:
            already_visited = visited_times.get(next, 0) > 0
            if not already_visited or 2 not in visited_times.values():
                visited_times[next] = visited_times.get(next, 0) + 1
                total += get_paths(adjacency, next, visited_times)
                visited_times[next] -= 1
        else:
            total += get_paths(adjacency, next, visited_times)
    return total


adjacency = {}
with open('input12.txt') as input_file:
    for line in input_file:
        if line == '\n':
            break
        a,b = line.strip().split('-')
        if a != 'end' and b != 'start':
            if a not in adjacency:
                adjacency[a] = []
            adjacency[a].append(b)
        if b != 'end' and a != 'start':
            if b not in adjacency:
                adjacency[b] = []
            adjacency[b].append(a)

print(get_paths(adjacency, 'start', {}))
