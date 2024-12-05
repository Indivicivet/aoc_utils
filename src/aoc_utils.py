from pathlib import Path

_data_folder = Path(__file__).parent.parent / "data"
_data_folder.mkdir(exist_ok=True, parents=True)


class YearLoader:
    def __init__(self, year):
        self.year = year


def __getattr__(name):
    if name and name[0] == "y":
        try:
            return YearLoader(int(name[1:]))
        except Exception as e:
            raise Exception("unknown year") from e
    raise AttributeError("Not a year")
