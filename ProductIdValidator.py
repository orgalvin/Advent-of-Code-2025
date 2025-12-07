class ProductIdValidator:
    sum_of_invalid_ids = 0

    def part_1(self, filepath):
        for r in self.extract_ranges_from_file(filepath):
            print(r)
            start, end = r.split('-')
            self.find_invalid_ids_part_1(int(start), int(end))

        print(f"Sum of invalid ids: {self.sum_of_invalid_ids}")

    def part_2(self, filepath):
        for r in self.extract_ranges_from_file(filepath):
            print(r)
            print()
            start, end = r.split('-')
            self.find_invalid_ids_part_2(int(start), int(end))

        print(f"Sum of invalid ids: {self.sum_of_invalid_ids}")

    def extract_ranges_from_file(self, filepath) -> [str]:
        with open(filepath, 'r') as file:
            csv = file.readline()
            return csv.split(',')

    def find_invalid_ids_part_1(self, start_range, end_range):

        for i in range(start_range, end_range + 1):
            i_str = str(i)
            i_length = len(i_str)
            # we can skip any numbers with an odd number of digits
            if i_length % 2 != 0:
                continue

            # split string into half
            first_half = i_str[:i_length // 2]
            second_half = i_str[i_length // 2:]
            print(f"{i}: {first_half} | {second_half}")

            old_sum = self.sum_of_invalid_ids
            # see if the two halves are identical and add if so
            if first_half == second_half:
                self.sum_of_invalid_ids += i
                print(f"adding {i} to sum: {old_sum} -> {self.sum_of_invalid_ids}")

    def find_invalid_ids_part_2(self, start_range, end_range):
        for i in range(start_range, end_range + 1):
            print(f"Processing {i}")
            i_str = str(i)
            i_length = len(i_str)

            # For each number in the input range, we will check for each combination of digits up to half
            for j in range(1, (i_length // 2) + 1):
                sub_str = i_str[:j]
                quotient, remainder = divmod(len(i_str), len(sub_str))

                # if the remainder is not 0, the substring could not be repeated to complete the total value
                if remainder != 0:
                    continue

                print(f"Testing substring {sub_str}")
                old_sum = self.sum_of_invalid_ids
                # repeat the string n number of times to get to the same number of digits as i
                if sub_str * quotient == i_str:
                    self.sum_of_invalid_ids += i
                    print(f"adding {i} to sum: {old_sum} -> {self.sum_of_invalid_ids}")
                    break
