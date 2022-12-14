# part 1
import re


def init_rocks():
    rocks = set()
    with open("input.txt") as fp:
        for line in fp:
            walls = [xy.split(",") for xy in re.findall(r"\d+,\d+", line)]

            prev_x, prev_y = int(walls[0][0]), int(walls[0][1])
            rocks.add((prev_x, prev_y))

            for curr_x, curr_y in walls[1:]:
                curr_x, curr_y = int(curr_x), int(curr_y)

                if prev_x == curr_x:  # horizontal wall
                    step = 1 if prev_y < curr_y else -1
                    for y in range(prev_y, curr_y, step):
                        rocks.add((curr_x, y))
                else:  # vertical wall
                    step = 1 if prev_x < curr_x else -1
                    for x in range(prev_x, curr_x, step):
                        rocks.add((x, curr_y))

                prev_x, prev_y = curr_x, curr_y
            rocks.add((prev_x, prev_y))  # last one in row not covered by range
    return rocks


def _move_sand(x, y, blocked):
    move_down = (x, y + 1)
    if move_down not in blocked:
        return move_down

    move_down_left = (x - 1, y + 1)
    if move_down_left not in blocked:
        return move_down_left

    move_down_right = (x + 1, y + 1)
    if move_down_right not in blocked:
        return move_down_right

    return None


def count_max_sand_units_before_void(blocked):
    endless_void_y = max(blocked, key=lambda x: x[1])[1]
    sand_counter = 0

    while True:
        sand_xy = (500, 0)

        while new_sand_xy := _move_sand(*sand_xy, blocked):
            if new_sand_xy[1] == endless_void_y:
                return sand_counter
            sand_xy = new_sand_xy

        blocked.add(sand_xy)
        sand_counter += 1


rocks = init_rocks()
print(count_max_sand_units_before_void(rocks.copy()))

# ----------------------------------------
# part 2
def count_max_sand_units_before_clogging(blocked):
    starting_point = (500, 0)
    min_sand_y = max(rocks, key=lambda x: x[1])[1] + 1
    sand_counter = 0

    while True:
        sand_xy = starting_point

        while new_sand_xy := _move_sand(*sand_xy, blocked):
            sand_xy = new_sand_xy
            if sand_xy[1] == min_sand_y:
                break

        blocked.add(sand_xy)
        sand_counter += 1

        if sand_xy == starting_point:
            return sand_counter


print(count_max_sand_units_before_clogging(rocks.copy()))
