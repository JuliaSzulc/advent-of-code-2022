# part 1
from collections import deque

with open("input.txt", "r") as fp:
    cubes = {tuple(int(c) for c in line.split(",")) for line in fp}


def adjacent_space(x, y, z):
    return {
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    }


surface_area = sum((adj not in cubes) for c in cubes for adj in adjacent_space(*c))

print(surface_area)

# ----------------------------------------
# part 2
# flood fill in space covering the droplet with additional space of 1 around
min_x, min_y, min_z = (min(c[i] for c in cubes) - 1 for i in range(3))
max_x, max_y, max_z = (max(c[i] for c in cubes) + 1 for i in range(3))
ranges = (
    range(min_x, max_x + 1),
    range(min_y, max_y + 1),
    range(min_z, max_z + 1),
)


def within_limits(coordinates):
    return all(c in rng for c, rng in zip(coordinates, ranges))


start = (min_x, min_y, min_z)
steam_cubes = {start}  # covered with steam
air_cubes_to_steam = deque([start])  # valid adjacent to current steam
surface_area = 0

while air_cubes_to_steam:
    new_steam_cube = air_cubes_to_steam.pop()

    for adj in adjacent_space(*new_steam_cube):  # find adjacent
        if within_limits(adj) and adj not in steam_cubes:
            if adj in cubes:
                surface_area += 1
            else:
                air_cubes_to_steam.appendleft(adj)
                steam_cubes.add(adj)  # cover with steam

print(surface_area)
