# part 1
from collections import deque
import re

with open("input.txt") as fp:
    state = [deque() for _ in range(9)]
    for i, line in enumerate(fp):
        if not line.strip().startswith("["):
            empty_line_idx = i + 2
            break

        for i, item in enumerate(re.findall("....?", line)):
            if (match := re.search(r"[A-Z]", item)):
                state[i].appendleft(match[0])

with open("input.txt") as fp:
    for line in fp.readlines()[empty_line_idx:]:
        num, src, dst = [int(x) for x in re.findall(r"[0-9]+", line)]
        src -= 1
        dst -= 1

        for _ in range(num):
            state[dst].append(state[src].pop())

print("".join([s.pop() for s in state]))

# ----------------------------------------
# part 2
with open("input.txt") as fp:
    state = [[] for _ in range(9)]
    for i, line in enumerate(fp):
        if not line.strip().startswith("["):
            empty_line_idx = i + 2
            break

        for i, item in enumerate(re.findall("....?", line)):
            if (match := re.search(r"[A-Z]", item)):
                state[i] = [match[0]] + state[i]

with open("input.txt") as fp:
    for line in fp.readlines()[empty_line_idx:]:
        num, src, dst = [int(x) for x in re.findall(r"[0-9]+", line)]
        src -= 1
        dst -= 1

        state[dst] += state[src][-num:]
        state[src] = state[src][:-num]

print("".join([s.pop() for s in state]))
