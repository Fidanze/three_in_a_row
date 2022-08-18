from three_in_a_row.crystal import Crystal
from .gameField import GameField


class OutputData:
    """Class for representation of console display"""

    def __init__(self, game_name: str, record: int, score: int, N: int = 5) -> None:
        self.game_name = game_name
        self.record = record
        self.score = score
        self.game_field = GameField(N, Crystal)
        self.command = ""
        self.is_started = False

    def __str__(self) -> str:
        result = ""
        result += f"Welcome to Nastya's game => {self.game_name}!\n"
        result += f"Your record: {self.record}!\n"
        result += f"Current score: {self.score}!\n"
        if self.is_started:
            result += str(self.game_field)
        result += self.command
        return result
