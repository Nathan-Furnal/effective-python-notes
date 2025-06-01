import re
from dataclasses import dataclass
from typing import Literal


@dataclass
class Move:
    direction: Literal["up", "down", "left", "right"]
    steps: int


def extract_move_from_directions(directions: str) -> Move | list[Move]:
    pat = re.compile(r"(down|up|left|right) by (\d+)")
    match res := pat.findall(directions):
        case [(direction, steps)]:
            return Move(direction, int(steps))
        case [*matches] if len(matches) > 0:
            return [Move(direction, int(steps)) for direction, steps in matches]
        case _:
            msg = f"Incorrect match: {res}"
            raise ValueError(msg)
