# part 1
from itertools import islice
import re

items_init = []  # to reset state for part 2
modulus = 1
monkeys = []

class Monkey():
    def __init__(self, operation, test_divisor, next_monkey_choice):
        self.items = []
        self.operation = operation
        self.test_divisor = test_divisor
        self.next_monkey_choice = next_monkey_choice
        self.inspection_counter = 0

    def _inspect_and_throw(self, old, manage_worry):  # needs to be named 'old' for eval
        worry = eval(self.operation)
        if manage_worry:
            worry = int(worry / 3)
        worry %= modulus

        next_monkey_i = self.next_monkey_choice[worry % self.test_divisor == 0]
        self.inspection_counter += 1

        return next_monkey_i, worry

    def run_round(self, manage_worry):
        throws = [self._inspect_and_throw(item, manage_worry) for item in self.items]
        return throws

with open("input.txt") as fp:
    while (monkey_info := list(islice(fp, 7))):  # 7 is number of lines per monkey info
        items = [int(item) for item in re.findall(r"\d+", monkey_info[1])]
        operation = "".join(monkey_info[2].split()[-3:])
        test_divisor = int(monkey_info[3].split()[-1])
        next_monkey_choice = {  # if is divisible
            True: int(monkey_info[4].split()[-1]),
            False: int(monkey_info[5].split()[-1]),
        }

        items_init.append(items)
        modulus *= test_divisor
        monkeys.append(Monkey(operation, test_divisor, next_monkey_choice))


def calculate_monkey_business_after_n_rounds(n, manage_worry=True):
    # init state
    for monkey, items_group in zip(monkeys, items_init):
        monkey.items = items_group.copy()
        monkey.inspection_counter = 0

    for _ in range(n):
        for monkey in monkeys:
            for next_monkey_i, item in monkey.run_round(manage_worry):
                monkeys[next_monkey_i].items.append(item)
            monkey.items = []

    inspection_counters = sorted([monkey.inspection_counter for monkey in monkeys])
    return inspection_counters[-1] * inspection_counters[-2]


print(calculate_monkey_business_after_n_rounds(20, manage_worry=True))

# ----------------------------------------
# part 2
print(calculate_monkey_business_after_n_rounds(10000, manage_worry=False))
