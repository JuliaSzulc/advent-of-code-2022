# part 1
with open("input.txt") as fp:
    priorities_sum = 0

    for line in fp:
        half_len = len(line) // 2
        item = set(line[:half_len]).intersection(line[half_len:]).pop()
        offset = 38 if item.isupper() else 96
        priorities_sum += ord(item) - offset

print(priorities_sum)

# ----------------------------------------
# part 2
with open("input.txt") as fp:
    lines = fp.readlines()
    priorities_sum = 0

    for group in zip(lines[::3], lines[1::3], lines[2::3]):
        badge = set(group[0].strip()).intersection(group[1], group[2]).pop()
        offset = 38 if badge.isupper() else 96
        priorities_sum += ord(badge) - offset

print(priorities_sum)
