from typing import List, Tuple

MAPPING = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

class Packet:
    def __init__(self, version: int, type_id: int):
        self.version = version
        self.type_id = type_id

class Literal(Packet):
    def __init__(self, version: int, value: int):
        Packet.__init__(self, version, 4)
        self.value = value

class Operator(Packet):
    def __init__(self, version: int, type_id: int, subpackets: List[Packet]):
        Packet.__init__(self, version, type_id)
        self.subpackets = subpackets

def parse_binary(binary: str) -> int:
    radix = 1
    sum = 0
    for digit in reversed(binary):
        sum += int(digit) * radix
        radix *= 2
    return sum

def parse_literal(substr: str) -> Tuple[int, int]:
    binary_groups = []
    group_type = None
    group_start = 0
    while group_type != '0':
        group_type = substr[group_start]
        group_contents = substr[group_start+1:group_start+5]
        binary_groups.append(group_contents)
        group_start += 5
    return parse_binary(''.join(binary_groups)), group_start

def parse_known_length(substr: str, subpacket_length: int) -> List[Packet]:
    subpackets = []
    subpacket_start = 0
    while subpacket_start < subpacket_length:
        subpacket, subpacket_size = parse_packet(substr[subpacket_start:])
        subpackets.append(subpacket)
        subpacket_start += subpacket_size
    return subpackets

def parse_known_count(substr: str, subpacket_count: int) -> Tuple[List[Packet], int]:
    subpackets = []
    parsed_count = 0
    parsed_length = 0
    while parsed_count < subpacket_count:
        subpacket, subpacket_size = parse_packet(substr[parsed_length:])
        subpackets.append(subpacket)
        parsed_count += 1
        parsed_length += subpacket_size
    return subpackets, parsed_length

def parse_packet(substr: str) -> Tuple[Packet, int]:
    version, type_id = parse_binary(substr[0:3]), parse_binary(substr[3:6])
    if type_id == 4:
        value, parsed_length = parse_literal(substr[6:])
        return Literal(version, value), 6 + parsed_length
    else:
        length_type_id = substr[6]
        if length_type_id == '0':
            subpacket_length, remainder = parse_binary(substr[7:22]), substr[22:]
            subpackets = parse_known_length(remainder, subpacket_length)
            packet_size = 22 + subpacket_length
        else:
            subpacket_count, remainder = parse_binary(substr[7:18]), substr[18:]
            subpackets, parsed_length = parse_known_count(remainder, subpacket_count)
            packet_size = 18 + parsed_length
        return Operator(version, type_id, subpackets), packet_size

def print_packet(packet: Packet, indent: int) -> None:
    if isinstance(packet, Literal):
        print('  ' * indent + 'Literal ' + str(packet.version) + ' ' + str(packet.value))
    else:
        print('  ' * indent + 'Operator ' + str(packet.version))
        for subpacket in packet.subpackets:
            print_packet(subpacket, indent + 1)

def sum_versions(packet: Packet) -> int:
    if isinstance(packet, Literal):
        return packet.version
    else:
        return packet.version + sum([sum_versions(subpacket) for subpacket in packet.subpackets])

def get_values(packet: Packet) -> List[int]:
    return [evaluate(subpacket) for subpacket in packet.subpackets]

def evaluate(packet: Packet) -> int:
    type_id = packet.type_id
    if type_id == 0:
        return sum(get_values(packet))
    elif type_id == 1:
        product = 1
        for value in get_values(packet):
            product *= value
        return product
    elif type_id == 2:
        return min(get_values(packet))
    elif type_id == 3:
        return max(get_values(packet))
    elif type_id == 4:
        return packet.value
    elif type_id == 5:
        values = get_values(packet)
        return 1 if values[0] > values[1] else 0
    elif type_id == 6:
        values = get_values(packet)
        return 1 if values[0] < values[1] else 0
    elif type_id == 7:
        values = get_values(packet)
        return 1 if values[0] == values[1] else 0
    else:
        raise Exception('Invalid type_id')


with open('input16.txt') as input_file:
    input = input_file.readline().strip()
    binary = ''.join([MAPPING[x] for x in input])

print(evaluate(parse_packet(binary)[0]))
