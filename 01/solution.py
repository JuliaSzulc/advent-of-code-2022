# part 1
with open("input.txt") as fp:
    max_total = 0
    total = 0

    for line in fp:
        if line == "\n":
            max_total = max(total, max_total)
            total = 0
        else:
            total += int(line)

print(max_total)

# ----------------------------------------
# part 2
with open("input.txt") as fp:
    totals = []
    total = 0

    for line in fp:
        if line == "\n":
            totals.append(total)
            total = 0
        else:
            total += int(line)

print(sum(sorted(totals)[-3:]))
