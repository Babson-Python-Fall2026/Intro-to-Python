import json
from pathlib import Path
def del_pems(state):
    pems = state['pems']

    DATA = (Path(__file__).parent.parent / "data").resolve()

    with open(DATA / "pems.json", "w", encoding="utf-8") as file:
                json.dump('', file, indent=2)