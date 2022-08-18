"""Realisation of game commands by using Enum"""
import enum
from functools import partial
import pickle
from typing import Any

from .data import OutputData


def help(data=None):
    data.command = """COMMMANDS:
    1) HELP => Show this manual
    2) START => Start game and generate field
    3) EXIT => End game
    4) SWAP => Swap to symbols, example: SWAP (1,2) (1,3)
    5) SAVE => Save current game to save.pickle file
    6) LOAD => Load previously saved game from save.pickle file
    """
    return data


def start(data: OutputData):
    data.is_started = True


def exit():
    pass


def swap(data: OutputData, xy1: tuple[int, int], xy2: tuple[int, int]):
    data.score += data.game_field.swap(xy1[1] - 1, xy1[0] - 1, xy2[1] - 1, xy2[0] - 1)
    if data.score > data.record:
        data.record = data.score
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

    HELP = partial(help)
    START = partial(start)
    EXIT = partial(exit)
    SAVE = partial(save)
    LOAD = partial(load)
    SWAP = partial(swap)

    def __call__(self, *args, **kwargs) -> Any:
        return self.value(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
