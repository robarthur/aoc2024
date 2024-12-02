from pathlib import Path
from collections import Counter
from typing import List


def get_input() -> list:
    file_name = Path(__file__.replace(".py", ".txt")).name
    file = Path(__file__).resolve().parents[1] / "input" / file_name
    with open(file, "r") as f:
        return f.read().splitlines()


def clean_data(data: list) -> "List[List[int]]":
    list_a = []
    list_b = []
    for d in data:
        a, b = d.split()
        list_a.append(a)
        list_b.append(b)
    return [sorted(list_a), sorted(list_b)]


def solve_part_1(data: "List[List[int]]") -> int:
    totalDistance = 0
    for i in zip(data[0], data[1]):
        totalDistance += abs(int(i[0]) - int(i[1]))
    return totalDistance


def solve_part_2(data: "List[List[int]]") -> int:
    similarity_score = 0
    list_b_counts = Counter(data[1])
    for location in data[0]:
        similarity_score += int(location) * int(list_b_counts[location])
    return similarity_score


def main():
    data = get_input()
    data = clean_data(data)
    print(f"location_id differences: {solve_part_1(data)}")
    print(f"similarity score: {solve_part_2(data)}")


if __name__ == "__main__":
    main()
