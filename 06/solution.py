# part 1
with open("input.txt") as fp:
    signal = fp.readline()

for i in range(4, len(signal)):
    if len(set(signal[(i - 4):i])) == 4:
        break
print(i)

# ----------------------------------------
# part 2
with open("input.txt") as fp:
    signal = fp.readline()

for i in range(14, len(signal)):
    if len(set(signal[(i - 14):i])) == 14:
        break
print(i)
