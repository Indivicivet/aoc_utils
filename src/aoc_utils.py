from pathlib import Path

_data_folder = Path(__file__).parent.parent / "data"
_data_folder.mkdir(exist_ok=True, parents=True)
