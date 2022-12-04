from collections import namedtuple

# part 1
Choice = namedtuple("Choice", ["X", "Y", "Z"])

score_table_1 = {
    "A": Choice(4, 8, 3),
    "B": Choice(1, 5, 9),
    "C": Choice(7, 2, 6),
}

with open("input.txt") as fp:
    total_score = 0

    for line in fp:
        opponent, me = line.split()
        total_score += getattr(score_table_1[opponent], me)

print(total_score)

# ----------------------------------------
# part 2
score_table_2 = {
    "A": Choice(3, 4, 8),
    "B": Choice(1, 5, 9),
    "C": Choice(2, 6, 7),
}

with open("input.txt") as fp:
    total_score = 0

    for line in fp:
        opponent, me = line.split()
        total_score += getattr(score_table_2[opponent], me)

print(total_score)
