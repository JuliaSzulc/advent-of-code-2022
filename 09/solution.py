# part 1
coordinates = {(0, 0)}
head = (0, 0)
tail = (0, 0)

move = {
    "R": lambda x: (x[0] + 1, x[1]),
    "L": lambda x: (x[0] - 1, x[1]),
    "U": lambda x: (x[0], x[1] + 1),
    "D": lambda x: (x[0], x[1] - 1),
}

with open("input.txt") as fp:
    movements = [line.split() for line in fp]

for direction, length in movements:
    for _ in range(int(length)):
        head = move[direction](head)

        diff_x = head[0] - tail[0]
        diff_y = head[1] - tail[1]

        if abs(diff_x) > 1 or abs(diff_y) > 1:
            if diff_x > 0:
                tail = move["R"](tail)
            elif diff_x < 0:
                tail = move["L"](tail)

            if diff_y > 0:
                tail = move["U"](tail)
            elif diff_y < 0:
                tail = move["D"](tail)

            coordinates.add(tail)

print(len(coordinates))

# ----------------------------------------
# part 2
coordinates = {(0, 0)}
knots = [(0, 0)] * 10

for direction, length in movements:
    for _ in range(int(length)):
        knots[0] = move[direction](knots[0])
        head = knots[0]

        for i in range(1, len(knots)):
            tail = knots[i]

            diff_x = head[0] - tail[0]
            diff_y = head[1] - tail[1]

            if abs(diff_x) > 1 or abs(diff_y) > 1:
                if diff_x > 0:
                    tail = move["R"](tail)
                elif diff_x < 0:
                    tail = move["L"](tail)

                if diff_y > 0:
                    tail = move["U"](tail)
                elif diff_y < 0:
                    tail = move["D"](tail)

            knots[i] = tail
            head = knots[i]

        coordinates.add(tail)

print(len(coordinates))
