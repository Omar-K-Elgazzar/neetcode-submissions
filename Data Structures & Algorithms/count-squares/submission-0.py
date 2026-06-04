from collections import defaultdict
from typing import List

class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        squares = 0

        for (x2, y2), freq in self.points.items():

            if x2 != x or y2 == y:
                continue

            side = abs(y2 - y)

            squares += (
                freq *
                self.points.get((x + side, y), 0) *
                self.points.get((x + side, y2), 0)
            )

            squares += (
                freq *
                self.points.get((x - side, y), 0) *
                self.points.get((x - side, y2), 0)
            )

        return squares