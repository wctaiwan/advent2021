from typing import Optional, Tuple

def intersect(
    p1: Tuple[int, int, int, int, int, int],
    p2: Tuple[int, int, int, int, int, int],
) -> Optional[Tuple[int, int, int, int, int, int]]:
    x1, x2, y1, y2, z1, z2 = p1
    x1p, x2p, y1p, y2p, z1p, z2p = p2
    if x1 > x2p or x2 < x1p or y1 > y2p or y2 < y1p or z1 > z2p or z2 < z1p:
        return None
    return (max(x1, x1p), min(x2, x2p), max(y1, y1p), min(y2, y2p), max(z1, z1p), min(z2, z2p))

boxes = []
with open('input22.txt') as input_file:
    for line in input_file:
        action, coords = line.strip().split(' ')
        xrange, yrange, zrange = coords.split(',')
        x1, x2 = [int(val) for val in xrange[2:].split('..')]
        y1, y2 = [int(val) for val in yrange[2:].split('..')]
        z1, z2 = [int(val) for val in zrange[2:].split('..')]
        bounds = (x1, x2, y1, y2, z1, z2)
        multiplier = 1 if action == 'on' else -1

        intersections = []
        for (other, other_multiplier) in boxes:
            intersection = intersect(bounds, other)
            if intersection is None:
                continue
            intersections.append((intersection, -other_multiplier))

        if multiplier == 1:
            boxes.append((bounds, 1))
        boxes.extend(intersections)

sum = 0
for (bounds, multiplier) in boxes:
    x1, x2, y1, y2, z1, z2 = bounds
    volume = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    if multiplier == 1:
        sum += volume
    else:
        sum -= volume

print(sum)
