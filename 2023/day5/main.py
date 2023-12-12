
# ❯ python -m day5.main
# [PERF] parse_input 0.648022 ms
# [PERF] part1 0.453234 ms
# Part 1:  111627841
# [PERF] part2 3.688812 ms
# Part 2:  69323688
import re
from dataclasses import dataclass

from utils import log_time


@dataclass
class Map:
    source: str
    dest: str
    mappings: tuple

    def map(self, value):
        return self.dest, self._find_mapping(value)

    def _find_mapping(self, value):
        for dst, src, count in self.mappings:
            if value in range(src, src + count):
                offset = value - src
                return dst + offset

        # default is identity mapping
        return value

    def map_range(self, value: tuple[int, int]):
        result = []
        toMap = [value]
        for m in self.mappings:
            next = []
            for tm in toMap:
                before, mapped, after = self._map_range(m, tm)
                if before:
                    next.append(before)
                if mapped:
                    result.append(mapped)
                if after:
                    next.append(after)
            toMap = next
        result.extend(toMap)  # include any last ranges that didn't get mapped
        return result

    def _map_range(self, mapping, source):
        dest, src, count = mapping

        def _diff(value):
            diff = value - src
            if diff >= 0 and diff < count:
                return dest + diff

        before, mapped, after = None, None, None
        start, end = src, src + count - 1
        if start > source[0]:
            before = (source[0], min(source[1], start - 1))
        if start <= source[1] and end >= source[0]:
            mapped = (_diff(max(source[0], start)), _diff(min(source[1], end)))
        if end < source[1]:
            after = (max(source[0], end + 1), source[1])
        return (before, mapped, after)


@log_time
def parse_input(lines):
    stanzas = lines.split("\n\n")
    seeds = parse_seeds(stanzas[0])
    maps = [parse_map(stanza.split("\n")) for stanza in stanzas[1:]]
    return seeds, maps


def parse_seeds(stanza):
    return list(map(int, re.findall(r"(\d+)", stanza)))


def parse_map(stanza):
    source, dest = re.findall(r"(\w+)-to-(\w+) map:", stanza[0])[0]
    ranges = [parse_range(r) for r in stanza[1:]]
    return Map(source, dest, ranges)


def parse_range(range_str):
    dst, src, count = map(int, re.findall(r"(\d+)", range_str))
    return dst, src, count


@log_time
def part1(seeds, maps):
    src_maps = {m.source: m for m in maps}

    def find_location(value):
        src = "seed"
        while src != "location":
            src, value = src_maps[src].map(value)

        return value

    return min(map(find_location, seeds))


@log_time
def part2(seeds, maps):
    seed_ranges = zip(seeds[::2], seeds[1::2])
    locations = []
    for pair in seed_ranges:
        ranges = [(pair[0], pair[0] + pair[1] - 1)]
        for m in maps:
            next = []
            for sr in ranges:
                # when a range is mapped, you can get a list of ranges back
                next += m.map_range(sr)
            ranges = next
            next = []
        locations.append(
            min(ranges)[0]  # take the beginning of min range as the lowest
        )
    return min(locations)


lines = open("day5/input.txt", encoding="utf8").read()

seeds, maps = parse_input(lines)
print("Part 1: ", part1(seeds, maps))
print("Part 2: ", part2(seeds, maps))
