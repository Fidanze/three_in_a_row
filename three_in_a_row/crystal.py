"""Realisation of game crystals by using Enum"""
import enum
from termcolor import colored


class Crystal(enum.Enum):
    """Enum for kind of crystals"""

    STAR = {"symbol": "*", "color": "yellow"}
    PLUS = {"symbol": "+", "color": "blue"}
    DOLLAR = {"symbol": "$", "color": "green"}
    CROSS = {"symbol": "X", "color": "red"}
    AT = {"symbol": "@", "color": "magenta"}

    def __init__(self, vals: dict[str, str]) -> None:
        self.symbol = vals["symbol"]
        self.color = vals["color"]

    def __str__(self) -> str:
        return colored(self.value["symbol"], self.value["color"])
