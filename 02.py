import re
with open("inputs\\input202102.txt") as f:
    log = f.readlines()

# Part_1
depth = 0
hor_pos = 0
pattern = "([a-z]+) ([0-9]+)"
for x in log:
    match = re.search(pattern, x)
    direction = match.group(1)
    number = int(match.group(2))
    if direction == "forward":
        hor_pos += number
    elif direction == "down":
        depth += number
    else:
        depth -= number
print("Solution Part1 -> " + str(depth*hor_pos))

# Part_2
depth = 0
hor_pos = 0
aim = 0
pattern = "([a-z]+) ([0-9]+)"
for x in log:
    match = re.search(pattern, x)
    direction = match.group(1)
    number = int(match.group(2))
    if direction == "forward":
        hor_pos += number
        depth += aim * number
    elif direction == "down":
        aim += number
    else:
        aim -= number
print("Solution Part2 -> " + str(depth*hor_pos))
