from three_in_a_row.crystal import Crystal
from .gameField import GameField
from three_in_a_row.cli import cli_redraw


class OutputData:
    """Class for representation of console display"""

    def __init__(self, game_name: str, record: int, score: int, N: int = 5) -> None:
        self.game_name = game_name
        self.record = record
        self._score = score
        self._game_field = GameField(N, Crystal)
        self._command = ""
        self.is_started = False

    @property
    def score(self):
        return self._score

    @score.setter  # type:ignore
    @cli_redraw
    def score(self, new_score):
        self._score = new_score

    @property
    def game_field(self):
        return self._game_field

    @game_field.setter  # type:ignore
    @cli_redraw
    def game_field(self, new_game_field):
        self._game_field = new_game_field

    @property
    def command(self):
        return self._command

    @command.setter  # type:ignore
    @cli_redraw
    def command(self, new_command):
        self._command = new_command

    def __str__(self) -> str:
        result = ""
        result += f"Welcome to Nastya's game => {self.game_name}!\n"
        result += f"Your record: {self.record}!\n"
        result += f"Current score: {self.score}!\n"
        if self.is_started:
            result += str(self.game_field)
        result += self.command
        return result
