# part 1
import math

heights = {}

with open("input.txt") as fp:
    for i, line in enumerate(fp):
        for j, char in enumerate(list(line.strip())):
            match char:
                case "S":
                    start = (i, j)
                    char = "a"
                case "E":
                    end = (i, j)
                    char = "z"
            heights[(i, j)] = ord(char)

def get_neighbors(row, col):
    return {
        (r, c)
        for r, c in [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]
        if (r, c) in heights.keys()
    }

def run_dijkstra(starting_point=start):
    not_visited = set(heights.keys())
    distances = {starting_point: 0}

    while (available := not_visited.intersection(distances)):
        current = min(available, key=lambda x: distances[x])

        distance = distances[current]
        if current == end:
            return distance

        not_visited.remove(current)

        neighbors = {
            n for n in get_neighbors(*current) if (heights[n] - heights[current] <= 1)
        }
        for neighbor in neighbors:
            distances[neighbor] = distance + 1

    return math.inf

print(run_dijkstra())

# ----------------------------------------
# part 2 stupid (~ 25 s)
# print(sorted([run_dijkstra(idx) for idx in heights if heights[idx] == ord("a")])[0])

# ----------------------------------------
# part 2 smart
def run_dijkstra_backwards(end_char, starting_point=end):
    end_value = ord(end_char)

    not_visited = set(heights.keys())
    distances = {starting_point: 0}

    while (available := not_visited.intersection(distances)):
        current = min(available, key=lambda x: distances[x])

        distance = distances[current]
        if heights[current] == end_value:
            return distance

        not_visited.remove(current)

        neighbors = {
            n for n in get_neighbors(*current) if (heights[n] - heights[current] >= -1)
        }
        for neighbor in neighbors:
            distances[neighbor] = distance + 1

    return math.inf

print(run_dijkstra_backwards(end_char="a"))
