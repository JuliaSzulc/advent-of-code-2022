# part 1
from itertools import cycle

with open("input.txt") as fp:
    symbols = fp.readline().strip()

# first quarter of the cartesian coordinate system; floor is y=0, left side is x=0
def init_rock():
    while True:
        # y - coordinate of the current highest rock
        # long horizontal
        yield lambda y: {(x, y + 4) for x in range(2, 6)}
        # cross
        yield lambda y: {(3, y + 4), (2, y + 5), (3, y + 5), (4, y + 5), (3, y + 6)}
        # reverse L
        yield lambda y: {(2, y + 4), (3, y + 4), (4, y + 4), (4, y + 5), (4, y + 6)}
        # long vertical
        yield lambda y: {(2, y + offset) for offset in range(4, 8)}
        # square
        yield lambda y: {(2, y + 4), (3, y + 4), (2, y + 5), (3, y + 5)}


def run(n_rocks):
    push_sequence = cycle(symbols)
    rock_generator = init_rock()

    rested_rocks = {(x, 0) for x in range(7)}  # init floor

    for _ in range(n_rocks):
        highest_rock_y = max({y for _, y in rested_rocks})
        rock_pos = next(rock_generator)(highest_rock_y)

        while True:
            # side push
            symbol = next(push_sequence)
            modifier = {"<": -1, ">": 1}[symbol]  # how to modify x
            limit = {"<": 0, ">": 6}[symbol]  # when rock can't be pushed further

            if all(x != limit for x, _ in rock_pos):
                new_rock_pos = {(x + modifier, y) for x, y in rock_pos}

                if all(xy not in new_rock_pos for xy in rested_rocks):
                    rock_pos = new_rock_pos

            # move down
            new_rock_pos = {(x, y - 1) for x, y in rock_pos}
            if any(xy in new_rock_pos for xy in rested_rocks):
                rested_rocks.update(rock_pos)  # previous position is rested
                break
            rock_pos = new_rock_pos

    return max({y for _, y in rested_rocks})


print(run(2022))
# ----------------------------------------
# part 2
