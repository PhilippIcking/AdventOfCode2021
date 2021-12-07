with open("inputs\\input202107.txt") as f:
    data_input = f.read().split(",")

positions = []
for x in data_input:
    positions.append(int(x))

# Part 1
cou_min = 100000000000000
for x in positions:
    akt_cou = 0
    for y in positions:
        akt_cou += abs(x-y)
    if akt_cou < cou_min:
        cou_min = akt_cou
print("Solution Part1 -> " + str(cou_min))


# Part 2
cou_min = 100000000000000
for x in range(sorted(positions).__getitem__(-1)):
    akt_cou = 0
    for y in positions:
        akt_cou += (abs(x-y)+1)*(abs(x-y)/2)
    if akt_cou < cou_min:
        cou_min = akt_cou
print("Solution Part2 -> " + str(int(cou_min)))
