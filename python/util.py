from pathlib import Path


def get_input() -> list:
    file_name = Path(__file__.replace(".py", ".txt")).name
    file = Path(__file__).resolve().parents[1] / "input" / file_name
    with open(file, "r") as f:
        return f.read().splitlines()
