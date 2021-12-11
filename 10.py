OPENINGS = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

VALUES = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def compute_score(stack):
    acc = 0
    for token in reversed(stack):
        acc *= 5
        acc += VALUES[token]
    return acc

input = []
with open('input10.txt') as input_file:
    for line in input_file:
        input.append(line.strip())

scores = []
for line in input:
    stack = []
    is_invalid = False
    for char in line:
        if char == '(' or char == '[' or char == '{' or char == '<':
            stack.append(char)
        else:
            if stack[-1] == OPENINGS[char]:
                stack.pop()
            else:
                is_invalid = True
                break
    if not is_invalid:
        scores.append(compute_score(stack))

scores = sorted(scores)
print(scores[len(scores) // 2])
