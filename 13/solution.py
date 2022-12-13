# part 1
with open("input.txt") as fp:
    packages = [eval(line.strip()) for line in fp if line != "\n"]

def compare_lists(left, right):
    result = 0  # -1 - unordered, 0 - equal, 1 - ordered

    for l, r in zip(left, right):
        match isinstance(l, list), isinstance(r, list):
            case True, True:
                result = compare_lists(l, r)
            case True, False:
                result = compare_lists(l, [r])
            case False, True:
                result = compare_lists([l], r)
            case False, False:
                if l != r:
                    return 1 if l < r else -1
        if result != 0:
            return result

    if len(left) == len(right):
        return 0
    return 1 if len(left) < len(right) else -1

result = 0
for i, pair in enumerate(zip(packages[::2], packages[1::2]), 1):
    if compare_lists(*pair) > 0:
        result += i

print(result)

# ----------------------------------------
# part 2
dividers = [[[2]], [[6]]]
packages.extend(dividers)

for i in range(len(packages) - 1):
    swaps_in_turn = False
    for j in range(len(packages) - 1 - i):
        if compare_lists(packages[j], packages[j + 1]) < 0:
            packages[j], packages[j + 1] = packages[j + 1], packages[j]
            swaps_in_turn = True
    if not swaps_in_turn:
        break

print((packages.index(dividers[0]) + 1) * (packages.index(dividers[1]) + 1))
