from enum import EnumMeta
from random import choice
from typing import Any


class GameField:
    def __init__(self, N: int, symbol_class: EnumMeta) -> None:
        self.symbol_class = symbol_class
        self.N = N
        self.field: list[list[Any]] = []
        for i in range(N):
            row: list[type] = []
            for j in range(N):
                el: type = choice(list(symbol_class))
                row.append(el)
            self.field.append(row)
        self.remove()

    def __len__(self) -> int:
        return self.N

    def __getitem__(self, item):
        return self.field[item]

    def __setitem__(self, item, value):
        self.field[item] = value

    def remove(self):
        count = 0
        while to_remove := self._get_triples():
            # removing
            for y, x in to_remove:
                count += 1
                self.field[y][x] = None

            # fall from up
            self.fall()

            # generate new symbols in None points
            for y in range(self.N):
                for x in range(self.N):
                    if self[y][x] == None:
                        self[y][x] = choice(list(self.symbol_class))
        return count

    def fall(self) -> None:
        for x in range(self.N):
            for y in range(self.N - 1, -1, -1):
                if self[y][x] == None:
                    for y_offset in range(y - 1, -1, -1):
                        if self[y_offset][x] != None:
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
            if self._get_triples():
                return self.remove()
            else:
                self[y2][x2], self[y1][x1] = self[y1][x1], self[y2][x2]
                return 0
        else:
            raise Exception("Symbols must be neighbors")

    def _get_triples(self) -> set[tuple[int, int]]:
        to_remove: set[Any] = set()

        for y in range(self.N):
            for x in range(self.N):
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
