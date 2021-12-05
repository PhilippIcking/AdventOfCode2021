import re

with open("inputs\\input202105.txt") as f:
    data_input = f.readlines()
pattern = "([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)"
vent_map = [[0 for x in range(1000)] for y in range(1000)]

# Part1
for x in range(len(data_input)):
    x_co = []
    y_co = []
    match = re.search(pattern, data_input[x])
    x1 = int(match.group(1))
    y1 = int(match.group(2))
    x2 = int(match.group(3))
    y2 = int(match.group(4))
    x_co.append(x1)
    x_co.append(x2)
    y_co.append(y1)
    y_co.append(y2)
    if x1 == x2 or y1 == y2:
        for a in range(min(x_co), max(x_co) + 1):
            for b in range(min(y_co), max(y_co) + 1):
                vent_map[a][b] = vent_map[a][b] + 1
cou = 0
for x in vent_map:
    for y in x:
        if y >= 2:
            cou += 1
print("Solution Part1 -> " + str(cou))

# Part2

vent_map = [[0 for x in range(1000)] for y in range(1000)]

for x in range(len(data_input)):
    x_co = []
    y_co = []
    match = re.search(pattern, data_input[x])
    x1 = int(match.group(1))
    y1 = int(match.group(2))
    x2 = int(match.group(3))
    y2 = int(match.group(4))
    x_co.append(x1)
    x_co.append(x2)
    y_co.append(y1)
    y_co.append(y2)
    if x1 == x2 or y1 == y2:
        for a in range(min(x_co), max(x_co) + 1):
            for b in range(min(y_co), max(y_co) + 1):
                vent_map[a][b] = vent_map[a][b] + 1
    else:
        k = 0
        l = 0
        for p in range(abs(x1 - x2) + 1):
            vent_map[x1 + k][y1 + l] = vent_map[x1 + k][y1 + l] + 1
            if x1 - x2 < 0:
                k += 1
            elif x1 - x2 > 0:
                k -= 1
            if y1 - y2 < 0:
                l += 1
            elif y1 - y2 > 0:
                l -= 1

cou = 0
for x in vent_map:
    for y in x:
        if y >= 2:
            cou += 1
print("Solution Part2 -> " + str(cou))
