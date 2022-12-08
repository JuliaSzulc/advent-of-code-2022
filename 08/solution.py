# part 1
with open("input.txt") as fp:
    rows = [[int(n) for nums in line.split() for n in nums] for line in fp]
cols = list(zip(*rows))

length = len(rows)
counter = 4 * (length - 1)  # outside "frame"

for i in range(1, length - 1):
    row = rows[i]
    for j in range(1, length - 1):
        col = cols[j]
        tree = row[j]

        tree_lines = [row[:j], row[j + 1:], col[:i], col[i + 1:]]  # from tree to edges
        counter += any(all(t < tree for t in tree_line) for tree_line in tree_lines)

print(counter)

# ----------------------------------------
# part 2
max_score = 0

for i in range(1, length - 1):
    row = rows[i]
    for j in range(1, length - 1):
        col = cols[j]
        tree = row[j]

        # from tree to edges (order matters)
        tree_lines = [row[:j][::-1], row[j + 1:], col[:i][::-1], col[i + 1:]]
        score = 1
        for tree_line in tree_lines:
            counter = 0
            for next_tree in tree_line:
                counter += 1
                if next_tree >= tree:
                    break
            score *= counter
        max_score = max(max_score, score)
print(max_score)
