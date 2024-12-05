from pathlib import Path
import inspect


def get_input() -> list:
    # Get the filename of the caller
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    file_name = Path(caller_file).stem + ".txt"

    # Construct the path to the input file
    file = Path(__file__).resolve().parents[1] / "input" / file_name
    with open(file, "r") as f:
        return f.read().splitlines()
