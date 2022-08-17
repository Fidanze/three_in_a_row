from enum import EnumMeta
from random import choice
from typing import Any

from three_in_a_row.crystal import Crystal


class GameField:
    def __init__(self, N: int, symbol_class: EnumMeta) -> None:
        self.field: list[list[Any]] = []
        for i in range(N):
            row: list[type] = []
            for j in range(N):
                el: type = choice(list(symbol_class))
                row.append(el)
            self.field.append(row)
        self.remove()
        self.N = N

    def remove(self, to_remove: set[tuple[int, int]]):

        while to_remove := self._get_triples():
            # removing
            for y, x in to_remove:
                self.field[y][x] = None

            # fall from up
            self.fall()

            # generate new symbols in None points
            for y in range(self.N):
                for x in range(self.N):
                    if self.field[y][x] == None:
                        self.field[y][x] = choice(list(Crystal))

    def fall(self) -> None:
        for x in range(self.N):
            for y in range(self.N - 1, -1, -1):
                if self.field[y][x] == None:
                    for y_offset in range(1, y):
                        set[tuple[int, int]]

    def swap(self, y1: int, x1: int, y2: int, x2: int) -> None:
        # checking neighborhood
        if (x1 == x2 and y1 in (y2 - 1, y2 + 1)) or (y1 == y2 and x1 in (x2 - 1, x2 + 1)):
            self.field[y1][x1], self.field[y2][x2] = self.field[y2][x2], self.field[y1][x1]
        else:
            raise Exception("Symbols must be neighbors")

    def _get_triples(self) -> set[tuple[int, int]]:
        to_remove: set[Any] = set()

        for y in range(self.N):
            for x in range(self.N):
                if y >= 2:
                    if (
                        len(
                            triple := {self.field[y][x], self.field[y - 1][x], self.field[y - 2][x]}
                        )
                        == 1
                    ):
                        to_remove.union(triple)
                if x >= 2:
                    if (
                        len(
                            triple := {self.field[y][x], self.field[y][x - 1], self.field[y][x - 2]}
                        )
                        == 1
                    ):
                        to_remove.union(triple)

        # horizontal checking
        for row_ind, row in enumerate(self.field):
            for el_ind, el in enumerate(row):
                if el_ind >= 2:
                    if el == row[el_ind - 1] == row[el_ind - 2]:
                        for i in range(el_ind - 2, el_ind + 1):
                            to_remove.add((row_ind, i))
        # vertical checking
        for row_ind, row in enumerate(self.field):
            for el_ind, el in enumerate(row):
                if row_ind >= 2:
                    if el == self.field[row_ind - 1][el_ind] == self.field[row_ind - 2][el_ind]:
                        for i in range(row_ind - 2, row_ind + 1):
                            to_remove.add((i, el_ind))
        return to_remove

    def __str__(self) -> str:
        result = ""
        for row in self.field:
            result += "".join(map(str, row)) + "\n"
        return result


a = GameField(5, Crystal)
print(a)
