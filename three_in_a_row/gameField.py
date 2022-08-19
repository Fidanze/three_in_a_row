from enum import EnumMeta, Enum
from random import choice
from typing import Any, Type

from three_in_a_row.cli import cli_redraw


class GameField:
    def __init__(self, N: int, symbol_class: EnumMeta) -> None:
        self.symbol_class = symbol_class
        self._field: list[list[Enum]] = [
            [choice(list(symbol_class)) for _ in range(N)] for _ in range(N)
        ]
        self.remove()

    @property
    def field(self):
        return self._field

    @field.setter  # type: ignore
    @cli_redraw
    def field(self, new_field):
        self._field = new_field

    def __len__(self) -> int:
        return len(self.field)

    def __getitem__(self, item) -> Any:
        return self.field[item]

    @cli_redraw
    def __setitem__(self, item, value) -> None:
        self.field[item] = value

    def remove(self) -> int:
        count = 0
        while to_remove := self._get_triples():
            # removing
            for y, x in to_remove:
                count += 1
                self.field[y][x] = None

            # fall from up
            self.fall()

            # generate new symbols in None points
            for y in range(len(self.field)):
                for x in range(len(self.field)):
                    if self[y][x] == None:
                        self[y][x] = choice(list(self.symbol_class))
        return count

    def fall(self) -> None:
        # run by columns
        for x in range(len(self.field)):
            # run in X-column from bottom to top
            for y in range(len(self.field) - 1, -1, -1):
                # search for deleted symbol
                if self[y][x] == None:
                    # search not deleted symbol in upper part X-column
                    for y_offset in range(y - 1, -1, -1):
                        if self[y_offset][x] != None:
                            # change them and continue to search of deleted symbol
                            self[y][x], self[y_offset][x] = (
                                self[y][x],
                                self[y_offset][x],
                            )
                            break

    def swap(self, y1: int, x1: int, y2: int, x2: int) -> int:
        # checking neighborhood
        if (x1 == x2 and (y1 == y2 - 1 or y1 == y2 + 1)) or (
            y1 == y2 and (x1 == x2 - 1 or x1 == x2 + 1)
        ):
            self[y1][x1], self[y2][x2] = self[y2][x2], self[y1][x1]
            # check is swap create any triple
            if self._get_triples():
                return self.remove()
            else:
                # repeat swap to rollback changes
                self[y1][x1], self[y2][x2] = self[y2][x2], self[y1][x1]
                return 0
        else:
            return -1

    def _get_triples(self) -> set[tuple[int, int]]:
        to_remove: set[Any] = set()

        for y in range(len(self.field)):
            for x in range(len(self.field)):
                if y >= 2:
                    if self[y][x] == self[y - 1][x] == self[y - 2][x]:
                        to_remove.add((y, x))
                        to_remove.add((y - 1, x))
                        to_remove.add((y - 2, x))
                if x >= 2:
                    if self[y][x] == self[y][x - 1] == self[y][x - 2]:
                        to_remove.add((y, x))
                        to_remove.add((y, x - 1))
                        to_remove.add((y, x - 2))
        return to_remove

    def __str__(self) -> str:
        result = ""
        for row in self.field:
            result += "".join(map(str, row)) + "\n"
        return result
