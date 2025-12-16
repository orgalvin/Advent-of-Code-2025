from typing import Any, List

from utils.Point import Point


class Map:
    def __init__(self):
        self.matrix: List[List[Any]] = []

    @classmethod
    def init_from_file(cls, filepath):
        instance = cls()
        with open(filepath, 'r') as file:
            for command in file:
                instance.matrix.append(list(command.strip()))

        return instance

    @property
    def width(self):
        return len(self.matrix[0])

    @property
    def height(self):
        return len(self.matrix)

    def value_at(self, point: Point):
        if point.x < 0 or point.x >= self.width:
            return None

        if point.y < 0 or point.y >= self.height:
            return None

        return self.matrix[point.y][point.x]

    def set_value_at(self, point: Point, value):
        if point.x < 0 or point.x >= self.width:
            return False

        if point.y < 0 or point.y >= self.height:
            return False

        self.matrix[point.y][point.x] = value
        return True

    def get_adjacent(self, point: Point):
        adjacent = [
            self.value_at(Point(point.x - 1, point.y - 1)),
            self.value_at(Point(point.x, point.y - 1)),
            self.value_at(Point(point.x + 1, point.y - 1)),
            self.value_at(Point(point.x - 1, point.y)),
            self.value_at(Point(point.x + 1, point.y)),
            self.value_at(Point(point.x - 1, point.y + 1)),
            self.value_at(Point(point.x, point.y + 1)),
            self.value_at(Point(point.x + 1, point.y + 1))
        ]

        return adjacent

    def print(self):
        for row in self.matrix:
            print(''.join(str(cell) for cell in row))
