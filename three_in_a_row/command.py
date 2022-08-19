"""Realisation of game commands by using Enum"""
from datetime import datetime
import enum
import pickle
import time
from functools import partial

from .data import OutputData


def help(data=None) -> str:
    return """COMMMANDS:
    1) HELP => Show this manual
    2) START => Start game and generate field
    3) EXIT => End game
    4) SWAP => Swap to symbols, example: SWAP (1,2) (1,3)
    5) SAVE => Save current game to save.pickle file
    6) LOAD => Load previously saved game from save.pickle file
    """


def start(data: OutputData) -> str:
    data.is_started = True
    return f"Start time: {datetime.now()}"


def exit(data: OutputData) -> str:
    save(data)
    return "Game was auto saved. See you later!"


def swap(data: OutputData) -> str:
    try:
        x1 = int(input("Write column number of first symbol: "))
        y1 = int(input("Write row number of first symbol: "))
        x2 = int(input("Write column number of second symbol: "))
        y2 = int(input("Write row number of second symbol: "))
    except:
        return "You should wwrite integers numbers, try again"
    points = data.game_field.swap(y1 - 1, x1 - 1, y2 - 1, x2 - 1)
    if points:
        data.score += points
        data.record = max(data.score, data.record)
        message = f"({x1}, {y1}) and ({x2}, {y2}) symbols was swapped"
    elif points == -1:
        message = "Symbols must be neighbors"
    else:
        message = "This swap did not create any triple!"
    return message


def load(data: OutputData) -> str:
    try:
        with open("save.pickle", "rb") as f:
            file_content = pickle.load(f)
            if file_content:
                data.is_started = True
                data.game_field = file_content.game_field
                data.score = file_content.score
                data.record = file_content.record
                return "Saved game was successfully load!"
            else:
                return "Save file is empty!"
    except:
        return "Save file was corrupted!"


def save(data) -> str:
    with open("save.pickle", "wb") as f:
        pickle.dump(data, f)
    return "Game was successfully saved!"


class Command(enum.Enum):
    """Enum for kind of commands"""

    HELP = partial(help)
    START = partial(start)
    EXIT = partial(exit)
    SAVE = partial(save)
    LOAD = partial(load)
    SWAP = partial(swap)

    def __call__(self, *args, **kwargs) -> str:
        return self.value(*args, **kwargs)

    def __eq__(self, __o: object) -> bool:
        return self.name.__eq__(__o)

    def __str__(self) -> str:
        return self.name
