# https://adventofcode.com/2025/day/4

from utils.Map import Map
from utils.Point import Point


class ForkliftOptimizer:
    map = Map()
    tot_accessible_rolls = 0

    def process_file(self, filepath):
        self.map = Map.init_from_file(filepath)

        self.extract_all_accessible_rolls()

        print(f"total accessible rolls : {self.tot_accessible_rolls}")

    def extract_all_accessible_rolls(self):
        cur_accessible_rolls = self.extract_accessible_rolls()
        self.tot_accessible_rolls += cur_accessible_rolls

        if cur_accessible_rolls > 0:
            self.extract_all_accessible_rolls()

    def extract_accessible_rolls(self):
        accessible_rolls = 0
        for x in range(self.map.width):
            for y in range(self.map.height):
                point = Point(x, y)

                if self.map.value_at(point) != "@":
                    print(f"skipping {x}, {y}")
                    continue

                adjacent = self.map.get_adjacent(point)
                if adjacent.count("@") < 4:
                    print(f"adding to count for available roll at {point.x}, {point.y} with adjacent {adjacent}")
                    accessible_rolls += 1
                    self.map.set_value_at(point, ".")

        return accessible_rolls




