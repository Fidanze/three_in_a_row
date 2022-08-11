from three_in_a_row.crystal import Crystal


class OutputData:
    """Class for representation of console display"""

    def __init__(self, game_name: str, record: int, score: int) -> None:
        self.game_name = game_name
        self.record = record
        self.score = score
        self.game_field = []
        self.command = ""

    def __str__(self) -> str:
        result = ""
        result += f"Welcome to Nastya's game => {self.game_name}!\n"
        result += f"Your record: {self.record}!\n"
        result += f"Current score: {self.score}!\n"
        for row in self.game_field:
            result += "".join(map(str, row)) + "\n"
        result += self.command
        return result
