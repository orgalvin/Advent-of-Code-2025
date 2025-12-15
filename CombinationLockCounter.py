# https://adventofcode.com/2025/day/1

class CombinationLockCounter:
    number_of_positions = 100

    def __init__(self):
        self.current_position = 50
        self.num_zeroes = 0

    def process_file(self, filepath):
        with open(filepath, 'r') as file:
            for command in file:
                self.parse_command(command)

        print(f"Password: {self.num_zeroes}")

    def parse_command(self, command):
        number_of_places = int(command[1:])
        print(f"{command}")

        full_rotations = number_of_places // self.number_of_positions
        net_num_places = number_of_places % self.number_of_positions

        self.add_full_rotations_to_count(full_rotations)

        if command[0] == "R":
            self.spin_right_and_check_for_crossings(net_num_places)
        elif command[0] == "L":
            self.spin_left_and_check_for_crossings(net_num_places)

        # find final valid position
        self.current_position = self.current_position % self.number_of_positions

    def add_full_rotations_to_count(self, full_rotations):
        self.num_zeroes += full_rotations
        print(f"adding {full_rotations} rotations")

    def spin_right_and_check_for_crossings(self, net_num_places):
        self.current_position = self.current_position + net_num_places

        if self.current_position >= self.number_of_positions:
            self.num_zeroes += 1
            print(f"adding 1 to count for pre-mod position {self.current_position}")

    def spin_left_and_check_for_crossings(self, net_num_places):
        starting_position = self.current_position
        self.current_position = self.current_position - net_num_places

        # If we start at 0, we are not crossing 0 with this rotation and we should not count it
        if self.current_position <= 0 and starting_position != 0:
            self.num_zeroes += 1
            print(f"adding 1 to count for pre-mod position {self.current_position}")
