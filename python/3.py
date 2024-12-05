import util
from typing import List, Tuple

import re

MULT_MATCH_PATTERN = re.compile(r'mul\((\d+),(\d+)\)')
DO_PATTERN = re.compile(r'do\(\)')
DONT_PATTERN = re.compile(r'don\'t\(\)')

def get_valid_muls_digit_pairs(data: str) -> List[Tuple[int, int]]:
    matches = MULT_MATCH_PATTERN.findall(data)
    return [(int(x), int(y)) for x, y in matches]

def sum_muls(data: List[Tuple[int, int]]) -> int:
    sum = 0
    for mul in data:
        sum += mul[0] * mul[1]
    return sum

def get_dont_ranges(data: str) -> List[Tuple[int, int]]:
    do_locations = sorted([match.end() for match in DO_PATTERN.finditer(data)])
    dont_locations = sorted([match.end() for match in DONT_PATTERN.finditer(data)])
    dont_ranges = []
    last_do = 0
    # Could we remove the need for two loops here
    # with a stack?
    for dont_location in dont_locations:
        found_do = False
        if dont_location < last_do:
            continue
        for do_location in do_locations:
            if do_location > dont_location:
                last_do = do_location
                dont_ranges.append((int(dont_location), (do_location)))
                found_do=True
                break
        # There's gotta be a better way to do this... but it's late
        if not found_do:
            dont_ranges.append((int(dont_location), len(data)))
    return dont_ranges

def remove_dont_data(data:str, dont_ranges: List[Tuple[int, int]]) -> str:
    # Reverse to avoid string index issues
    for start, end in sorted(dont_ranges, reverse=True):
        data = data[:start] + data[end:]
    return data

def main():
    data = util.get_input()
    # Tricked me with multiple lines...
    data="".join(data)
    valid_muls=get_valid_muls_digit_pairs(data)

    print(f"part1: {sum_muls(valid_muls)}")

    dont_ranges = get_dont_ranges(data)
    print(dont_ranges)
    data = remove_dont_data(data, dont_ranges)
    print(data)
    valid_muls=get_valid_muls_digit_pairs(data)
    print(valid_muls)
    print(f"part2: {sum_muls(valid_muls)}")

if __name__ == "__main__":
    main()
