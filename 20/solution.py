# part 1
def mix(nums):
    len_nums = len(nums)
    for _ in range(len_nums):
        i = next(i for i, (_, mixed) in enumerate(nums) if not mixed)
        num = nums.pop(i)[0]

        if (new_idx := (i + num) % (len_nums - 1)) == 0:
            new_idx = len_nums - 1

        nums.insert(new_idx, (num, True))
    return nums


def get_grove_coord(nth, mixed):
    zero_index = mixed.index((0, True))
    if (zero_to_start := len(mixed) - zero_index) > nth:
        return mixed[zero_index + nth][0]
    return mixed[(nth - zero_to_start) % len(mixed)][0]


with open("input.txt") as fp:
    # list of tuples (num, is_mixed)
    initial_nums = [(int(num), False) for num in fp.readlines()]

mixed = mix(initial_nums)
print(sum(get_grove_coord(n * 1000, mixed) for n in [1, 2, 3]))

# ----------------------------------------
# part 2
