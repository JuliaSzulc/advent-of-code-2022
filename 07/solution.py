# part 1
pwd = ""
dir_sizes = {}

with open("input.txt") as fp:
    for line in fp:
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "..":
                    pwd = pwd.rsplit("/", maxsplit=1)[0]
                else:
                    pwd = "" if line[2] == "/" else pwd + "/" + line[2]
                    if pwd not in dir_sizes:
                        dir_sizes[pwd] = 0
        elif (size := line[0]) != "dir":
            dir_sizes[pwd] += int(size)

for path in sorted(dir_sizes.keys(), key=lambda x: x.count("/"), reverse=True):
    if (size := dir_sizes[path]):
        parent = path.rsplit("/", 1)[0]
        dir_sizes[parent] += size

print(sum(size for size in dir_sizes.values() if size <= 100000))

# ----------------------------------------
# part 2
with open("input.txt") as fp:
    used = sum(int(size) for line in fp if (size := line.split()[0]) not in ["$", "dir"])
needed = 30000000 - (70000000 - used)

print(sorted(size for size in dir_sizes.values() if size > needed)[0])
