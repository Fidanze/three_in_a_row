from __future__ import annotations

import os
from re import L
import time
from typing import Any


class CLI:
    consoles: dict[Any, CLI] = {}

    @classmethod
    def add(cls, data: Any) -> None:
        cls.consoles[data] = cls(data)

    def __init__(self, data: Any) -> None:
        self.data = data

    def draw(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print(self.data)
        time.sleep(3)


def cli_redraw(func):
    def wrapper(self, *args, **kwargs) -> Any:
        func(self, *args, **kwargs)
        if hasattr(self, "game_field"):
            CLI.consoles[self].draw()
        else:
            for key in CLI.consoles.keys():
                if key.game_field == self:
                    CLI.consoles[key].draw()
                    break

    return wrapper
