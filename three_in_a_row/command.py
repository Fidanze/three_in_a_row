"""Realisation of game commands by using Enum"""
import enum
import pickle
from typing import Any
from random import choice
from three_in_a_row.crystal import Crystal

from .data import OutputData


def help(data=None):
    commands_info = """COMMMANDS:
    1) HELP => Show this manual
    2) START => Start game and generate field
    3) EXIT => End game
    4) SWAP => Swap to symbols, example: SWAP (1,2) (1,3)
    5) SAVE => Save current game to save.pickle file
    6) LOAD => Load previously saved game from save.pickle file
    """

    data.command = commands_info
    return data


def get_start_field():
    return [[choice(list(Crystal)) for _ in range(5)] for _ in range(5)]


def start(data: OutputData):
    game_field: list[list[Crystal]] = []
    for i in range(5):
        row: list[Crystal] = []
        for j in range(5):
            el = choice(list(Crystal))
            if j >= 2:
                while el == row[-1] == row[-2]:
                    el = choice(list(Crystal))
            row.append(el)
        game_field.append(row)
    data.game_field = game_field


def exit():
    pass


def swap(data: OutputData, xy1: tuple[int, int], xy2: tuple[int, int]):
    xy1 = (xy1[1] - 1, xy1[0] - 1)
    xy2 = (xy2[1] - 1, xy2[0] - 1)
    n = len(data.game_field)
    if any(map(lambda x: x not in range(0, n), [*xy1, *xy2])):
        data.command = f"Incorrect coordinates of crystals: {xy1} and {xy2}"
    else:
        temp = data.game_field[xy1[0]][xy1[1]]
        data.game_field[xy1[0]][xy1[1]] = data.game_field[xy2[0]][xy2[1]]
        data.game_field[xy2[0]][xy2[1]] = temp
    return data


def load():
    try:
        with open("save.pickle", "rb") as f:
            file_content = pickle.load(f)
            if file_content:
                return file_content
            return file_content
    except:
        return None


def save(data):
    with open("save.pickle", "wb") as f:
        pickle.dump(data, f)


class Command(enum.Enum):
    """Enum for kind of commands"""

    HELP = {"func": help, "kwargs": dict()}
    START = {"func": start, "kwargs": dict()}
    EXIT = {"func": exit, "kwargs": dict()}
    SAVE = {"func": save, "kwargs": dict()}
    LOAD = {"func": load, "kwargs": dict()}
    SWAP = {"func": swap, "kwargs": dict()}

    def __init__(self, vals: dict[str, Any]) -> None:
        self.func = vals["func"]
        self.args = vals["kwargs"]

    def __str__(self) -> str:
        return self.name
