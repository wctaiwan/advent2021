from typing import List, Dict

digit_to_number = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9',
}

def get_wire_mapping(digits: List[str]) -> Dict[str, str]:
    actual_to_wire = {}
    wire_to_count = {x: 0 for x in 'abcdefg'}
    one_wires, four_wires, seven_wires = None, None, None

    for digit in digits:
        if len(digit) == 2:
            one_wires = {x for x in digit}
        elif len(digit) == 3:
            seven_wires = {x for x in digit}
        elif len(digit) == 4:
            four_wires = {x for x in digit}
        for wire in digit:
            wire_to_count[wire] += 1

    for wire, count in wire_to_count.items():
        if count == 4:
            actual_to_wire['e'] = wire
        elif count == 6:
            actual_to_wire['b'] = wire
        elif count == 9:
            actual_to_wire['f'] = wire

    actual_to_wire['a']  = (seven_wires - one_wires).pop()
    actual_to_wire['c'] = (one_wires - {actual_to_wire['f']}).pop()
    actual_to_wire['d'] = (
        four_wires - {actual_to_wire['b'], actual_to_wire['c'], actual_to_wire['f']}
    ).pop()
    actual_to_wire['g'] = ({x for x in 'abcdefg'} - set(actual_to_wire.values())).pop()

    return {wire: actual for actual, wire in actual_to_wire.items()}

def translate(digit: str, wire_mapping: Dict[str, str]) -> str:
    translated_digit = ''.join(sorted([wire_mapping[wire] for wire in digit]))
    return digit_to_number[translated_digit]

input = []
with open('input8.txt') as input_file:
    for line in input_file:
        digits, value = [part.strip().split() for part in line.split('|')]
        input.append((digits, value))

sum = 0
for digits, value in input:
    wire_mapping = get_wire_mapping(digits)
    sum += int(''.join([translate(digit, wire_mapping) for digit in value]))
print(sum)
