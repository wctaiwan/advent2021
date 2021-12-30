from typing import List, Tuple

wins = {}

rolls = []
for i in range(1, 4):
    for j in range(1, 4):
        for k in range(1, 4):
            rolls.append(i+j+k)

def play(p1: int, p2: int, s1: int, s2: int) -> Tuple[int, int]:
    global wins
    input = (p1, p2, s1, s2)
    if input in wins:
        return wins[input]

    w1, w2 = 0, 0
    for r1 in rolls:
        p1, p2, s1, s2 = input
        p1 += r1
        p1 = (p1 - 1) % 10 + 1
        s1 += p1
        if s1 >= 21:
            w1 += 1
            continue

        for r2 in rolls:
            p2, s2 = input[1], input[3]
            p2 += r2
            p2 = (p2 - 1) % 10 + 1
            s2 += p2
            if s2 >= 21:
                w2 += 1
                continue

            # The game does not end in the current round given r1, r2
            n1, n2 = play(p1, p2, s1, s2)
            w1 += n1
            w2 += n2

    wins[input] = (w1, w2)
    return w1, w2

print(play(3, 10, 0, 0))
