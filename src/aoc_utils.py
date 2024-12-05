from pathlib import Path

_data_folder = Path(__file__).parent.parent / "data"
_data_folder.mkdir(exist_ok=True, parents=True)


def __getattr__(name):
    if name and name[0] == "y":
        return f"year_{name}"
    raise AttributeError("Not a year")
