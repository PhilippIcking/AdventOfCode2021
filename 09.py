with open("inputs\\input202109.txt") as f:
    input_data = f.read().split("\n")

# Part 1
cou_p1 = 0
low_points = []
for x in range(len(input_data)):
    for y in range(len(input_data[x])):
        near_numbs = []
        if x - 1 >= 0:
            near_numbs.append(int(input_data[x - 1][y]))
        if y - 1 >= 0:
            near_numbs.append(int(input_data[x][y - 1]))
        try:
            near_numbs.append(int(input_data[x + 1][y]))
        except IndexError:
            pass
        try:
            near_numbs.append(int(input_data[x][y + 1]))
        except IndexError:
            pass
        near_numbs.append(int(input_data[x][y]))
        near_numbs = sorted(near_numbs)
        if near_numbs[0] == int(input_data[x][y]) and int(input_data[x][y]) < near_numbs[1]:
            cou_p1 += 1 + int(input_data[x][y])
            low_points.append((x, y))

print("Solution Part1 -> " + str(cou_p1))


# Part 2


def getbasinsize(x, input_data):
    basinsize = 0
    basinsize += 1
    used_coor = [x]
    found = False
    while not found:
        akt_coor = []
        for spots in used_coor:
            row = spots[0]
            col = spots[1]
            if (row - 1) >= 0 and int(input_data[abs(row - 1)][col]) != 9 and (row - 1, col) not in used_coor:
                akt_coor.append((row - 1, col))
            if (col - 1) >= 0 and int(input_data[row][abs(col - 1)]) != 9 and (row, col - 1) not in used_coor:
                akt_coor.append((row, col - 1))
            try:
                if int(input_data[row + 1][col]) != 9 and (row + 1, col) not in used_coor:
                    akt_coor.append((row + 1, col))
            except IndexError:
                pass
            try:
                if int(input_data[row][col + 1]) != 9 and (row, col + 1) not in used_coor:
                    akt_coor.append((row, col + 1))
            except IndexError:
                pass
        used_coor = used_coor + akt_coor
        if len(akt_coor) == 0:
            found = True
            return len(set(used_coor))


basins_sizes = []
for x in low_points:
    basins_sizes.append(getbasinsize(x, input_data))
basins_sizes = sorted(basins_sizes)
print("Solution Part2 -> " + str(basins_sizes[-3] * basins_sizes[-2] * basins_sizes[-1]))
