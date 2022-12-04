import re

# part 1
with open("input.txt") as fp:
    counter = 0

    for line in fp:
        line = [int(x) for x in re.split(",|-", line)]

        first = set(range(line[0], line[1] + 1))
        second = set(range(line[2], line[3] + 1))

        counter += first.issubset(second) or second.issubset(first)

print(counter)

# ----------------------------------------
# part 2
with open("input.txt") as fp:
    counter = 0

    for line in fp:
        line = [int(x) for x in re.split(",|-", line)]

        first = set(range(line[0], line[1] + 1))
        second = set(range(line[2], line[3] + 1))

        counter += bool(first.intersection(second))

print(counter)
