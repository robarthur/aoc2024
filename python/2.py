import util
from typing import List


def clean_data(data: list) -> List[List[int]]:
    return [l.split() for l in data]


def is_safe_level(level: List[int]) -> bool:
    difference_list = [int(level[i]) - int(level[i - 1]) for i in range(1, len(level))]
    return max(map(abs, difference_list)) <= 3 and (
        all(d > 0 for d in difference_list) or all(d < 0 for d in difference_list)
    )


def solve_part_1(data: List[List[int]]) -> int:
    return sum(1 for level in data if is_safe_level(level))


def solve_part_2(data: List[List[int]]) -> int:
    safe_count = 0
    for level in data:
        for i in range(len(level)):
            sublist = level[:i] + level[i + 1 :]
            if is_safe_level(sublist):
                safe_count += 1
                # No need to check further; this level is considered safe
                break
    return safe_count


def main():
    data = util.get_input()
    data = clean_data(data)
    print(f"valid levels: {solve_part_1(data)}")
    print(f"valid 'dampened' levels: {solve_part_2(data)}")


if __name__ == "__main__":
    main()
