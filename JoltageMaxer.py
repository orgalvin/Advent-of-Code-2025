# https://adventofcode.com/2025/day/3

class JoltageMaxer:
    total_joltage = 0

    def process_file(self, filepath, num_batteries):
        with open(filepath, 'r') as file:
            for command in file:
                bank = command.strip()
                self.total_joltage += self.find_max_joltage_for_bank(bank, num_batteries)

        print(f"total output joltage: {self.total_joltage}")

    def find_max_joltage_for_bank(self, bank, num_batteries):
        bank_joltage = ''
        # The left bound establishes the digit after the last selected digit
        left_bound = 0
        # The right bound lets us look through as many digits as we can while leaving enough digits remaining for us
        # to use num_batteries of digits
        right_bound = len(bank) - num_batteries + 1

        for i in range(num_batteries):
            sub_bank = bank[left_bound:right_bound]
            print(f"processing sub_bank {sub_bank}")
            sub_max, loc = self.find_max(sub_bank)
            left_bound += loc + 1
            bank_joltage += sub_max
            right_bound += 1

        print(f"Found joltage {bank_joltage} for bank {bank}")
        return int(bank_joltage)

    def find_max(self, sub_bank):
        max_joltage = sorted(list(sub_bank), reverse=True)[0]
        loc = sub_bank.find(max_joltage)

        print(f"[find_max] {max_joltage}, {loc}")

        return max_joltage, loc