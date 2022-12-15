# part 1
import re


class Sensor:
    def __init__(self, x, y, beacon):
        self.x = x
        self.y = y
        self.beacon = beacon
        self.max_dist = self.manhattan_dist(*beacon)

    def manhattan_dist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)


sensors, beacons = [], []
with open("input.txt") as fp:
    for line in fp:
        s_x, s_y, b_x, b_y = [int(number) for number in re.findall(r"-?\d+", line)]

        sensors.append(Sensor(s_x, s_y, (b_x, b_y)))
        beacons.append((b_x, b_y))


def invalid_x_in_y(chosen_y):
    invalid_x = set()
    for s in sensors:
        if (y_diff := abs(chosen_y - s.y)) <= s.max_dist:
            x_diff = s.max_dist - y_diff  # in chosen_y
            invalid_x.update(set(range((s.x - x_diff), (s.x + x_diff + 1))))

    invalid_x.difference_update({b[0] for b in beacons if b[1] == chosen_y})

    return invalid_x


print(len(invalid_x_in_y(2000000)))

# ----------------------------------------
# part 2
def find_beacon(lower_limit, upper_limit):
    for s in sensors:
        outer_dist = s.max_dist + 1  # closest points NOT within the sensor's range

        for x in range((s.x - outer_dist), (s.x + outer_dist + 1)):
            if x < lower_limit or x > upper_limit:
                continue
            y_diff = outer_dist - abs(x - s.x)

            for y in [(s.y - y_diff), (s.y + y_diff)]:
                if y < lower_limit or y > upper_limit or (x, y) in beacons:
                    continue

                if all(s_.manhattan_dist(x, y) > s_.max_dist for s_ in sensors):
                    return (x, y)


x, y = find_beacon(0, 4000000)
print(4000000 * x + y)
