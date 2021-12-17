from typing import List, Type
from utils import log_time, chunk
from dataclasses import dataclass, field
from math import prod


@dataclass
class Packet:
    type: int
    version: int
    num: int = 0
    sub: List[Type["Packet"]] = field(default_factory=list)


def parse_num(packet):
    bits = ""
    consumed = 0
    for c in chunk(packet, 5):
        consumed += 5
        bits += c[1:]

        if c[0] == "0":
            break
    return int(bits, 2), consumed


def parse_packet(b):
    if int(b) == 0:
        return  # just padding

    packet = Packet(version=int(b[:3], 2), type=int(b[3:6], 2))
    consumed = 6

    if packet.type == 4:
        n, c = parse_num(b[6:])
        packet.num = n
        consumed += c
        return packet, consumed

    else:
        r, c = parse_operator(b[6:])
        packet.sub = r
        consumed += c
        return packet, consumed


def parse_operator(b):
    length_type = b[0]
    consumed = 1

    if length_type == "0":
        length = int(b[1:16], 2)
        consumed += 15

        packets = []
        full_packet = consumed + length
        while consumed != full_packet:
            r, c = parse_packet(b[consumed:consumed+length])
            consumed += c
            packets.append(r)
        return packets, consumed

    else:
        length = int(b[1:12], 2)
        consumed += 11
        packets = []
        for _ in range(length):
            r, c = parse_packet(b[consumed:])
            consumed += c
            packets.append(r)
        return packets, consumed


def gt(l):
    a, b = l
    if a > b:
        return 1
    return 0


def lt(l):
    a, b = l
    if a < b:
        return 1
    return 0


def eq(l):
    a, b = l
    if a == b:
        return 1
    return 0


ops = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: gt,
    6: lt,
    7: eq
}


def run(packet):
    if packet.type == 4:
        return packet.num
    return ops[packet.type]([run(p) for p in packet.sub])


@ log_time
def part_a(input):
    fill = len(input) * 4
    bit_list = bin(int(input, 16))[2:].zfill(fill)
    packets, _ = parse_packet(bit_list)

    def sum_version(p):
        s = p.version
        for sub in p.sub:
            s += sum_version(sub)
        return s

    return sum_version(packets)


@ log_time
def part_b(input):
    fill = len(input) * 4
    bit_list = bin(int(input, 16))[2:].zfill(fill)
    packets, _ = parse_packet(bit_list)

    return run(packets)


input = open('day16/input.txt').read().strip()


result_a = part_a(input)
result_b = part_b(input)
print("Part A:", result_a)
print("Part B:", result_b)
