from math import ceil, floor
from typing import List, Optional, Union

TokenList = List[Union[str, int]]

def parse(input: str) -> TokenList:
    result = []
    pos = 0
    while pos < len(input):
        if input[pos] >= '0' and input[pos] <= '9':
            num_str = input[pos]
            pos += 1
            while input[pos] >= '0' and input[pos] <= '9':
                num_str += input[pos]
                pos += 1
            result.append(int(num_str))
        else:
            result.append(input[pos])
            pos += 1
    return result

def add(first: TokenList, second: TokenList) -> TokenList:
    result: TokenList = [] # Work around typing issue
    return result + ['['] + first + [','] + second + [']']

def add_to_last(tokens: TokenList, number: int) -> None:
    pos = len(tokens) - 1
    while pos >= 0:
        if isinstance(tokens[pos], int):
            tokens[pos] = tokens[pos] + number # type: ignore
            break
        pos -= 1

def add_to_first(tokens: TokenList, number: int) -> None:
    pos = 0
    while pos < len(tokens):
        if isinstance(tokens[pos], int):
            tokens[pos] = tokens[pos] + number # type: ignore
            break
        pos += 1

def explode(input: TokenList) -> Optional[TokenList]:
    pos = 0
    open_count = 0
    while pos < len(input):
        if input[pos] == '[':
            open_count += 1
        if input[pos] == ']':
            open_count -= 1
        if open_count == 5:
            left_num = input[pos+1]
            assert isinstance(left_num, int)
            right_num = input[pos+3]
            assert isinstance(right_num, int)
            left = input[:pos]
            right = input[pos+5:]
            add_to_last(left, left_num)
            add_to_first(right, right_num)
            return left + [0] + right
        pos += 1
    return None

def split(input: TokenList) -> Optional[TokenList]:
    pos = 0
    while pos < len(input):
        if isinstance(input[pos], int):
            number = input[pos]
            assert isinstance(number, int)
            if number >= 10:
                left_num = floor(number/2)
                right_num = ceil(number/2)
                return input[:pos] + ['[', left_num, ',', right_num, ']'] + input[pos+1:]
        pos += 1
    return None

def reduce(input: TokenList) -> TokenList:
    previous = input
    did_reduce = True
    while did_reduce:
        did_reduce = False
        reduced = explode(previous)
        if reduced is not None:
            previous = reduced
            did_reduce = True
            continue
        reduced = split(previous)
        if reduced is not None:
            previous = reduced
            did_reduce = True
    return previous

def magnitude(input: TokenList) -> int:
    if isinstance(input[0], int):
        return input[0]
    open_count = 1
    comma_count = 0
    pos = 0
    while comma_count < open_count:
        pos += 1
        if input[pos] == '[':
            open_count += 1
        elif input[pos] == ',':
            comma_count += 1
    return 3 * magnitude(input[1:pos]) + 2 * magnitude(input[pos+1:-1])

input = []
with open('input18.txt') as input_file:
    for line in input_file:
        if line == '\n':
            break
        input.append(parse(line.strip()))

max_sum = 0
for i in range(len(input)):
    for j in range(i+1, len(input)):
        max_sum = max(
            max_sum,
            magnitude(reduce(add(input[i], input[j]))),
            magnitude(reduce(add(input[j], input[i]))),
        )
print(max_sum)
