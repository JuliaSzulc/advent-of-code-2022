# part 1
with open("input.txt") as fp:
    program = [line.split() for line in fp]

x_values = [1]  # x AFTER nth cycle (during n+1 cycle)

for instruction in program:
    x = x_values[-1]

    if len(instruction) == 1:  ## noop
        x_values.append(x)
    else:  # addx
        x_values.extend([x, x + int(instruction[1])])

# taking i-1 index since it needs to be state during that cycle
print(sum(i * x_values[i - 1] for i in range(20, 241, 40)))

# ----------------------------------------
# part 2
crt = [(["."] * 40).copy() for _ in range(6)]

for cycle in range(241):
    row, position = divmod(cycle, 40)
    x = x_values[cycle]
    sprite = [x, x + 1, x + 2]

    if (position + 1) in sprite:
        crt[row][position] = "#"

for row in crt:
    print("".join(row))
