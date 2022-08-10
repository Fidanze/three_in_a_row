from typing import Any


class OutputData:
    """Data representation of console display"""

    def __init__(self, greeting: str, record: int, score: int, game_field: list[list[Any]]) -> None:
        self.greeting = greeting
        self.record = record
        self.score = score
        self.game_field = game_field

    def __str__(self) -> str:
        result = ""
        result += f"Welcome to Nastya's game => {self.greeting} !\n"
        result += f"Your record: {self.record} !\n"
        result += f"Current score: {self.score} !\n"
        for row in self.game_field:
            result += "".join(map(str, row)) + "\n"
        return result
