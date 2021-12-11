with open("inputs\\input202111.txt") as f:
    data_input = f.read().split("\n")
matrix = []
cou_p1 = 0
for x in range(len(data_input)):
    matrix.append([])
    for y in data_input[x]:
        matrix[x].append(int(y))


def check_index(x, y):
    if matrix[x][y] > 9 and not flashed_indexes.__contains__((x, y)):
        flashed_indexes.append((x, y))
        if (x - 1) >= 0 and (y - 1) >= 0:
            matrix[x - 1][y - 1] += 1
            check_index(x - 1, y - 1)
        if (x - 1) >= 0:
            matrix[x - 1][y] += 1
            check_index(x - 1, y)
        if (x - 1) >= 0 and (y + 1) < len(matrix[x]):
            matrix[x - 1][y + 1] += 1
            check_index(x - 1, y + 1)
        if (y - 1) >= 0:
            matrix[x][y - 1] += 1
            check_index(x, y - 1)
        if (y + 1) < len(matrix[x]):
            matrix[x][y + 1] += 1
            check_index(x, y + 1)
        if (x + 1) < len(matrix) and (y - 1) >= 0:
            matrix[x + 1][y - 1] += 1
            check_index(x + 1, y - 1)
        if (x + 1) < len(matrix):
            matrix[x + 1][y] += 1
            check_index(x + 1, y)
        if (x + 1) < len(matrix) and (y + 1) < len(matrix[x]):
            matrix[x + 1][y + 1] += 1
            check_index(x + 1, y + 1)
    else:
        pass


# Part 1
for i in range(100):
    flashed_indexes = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] += 1
            check_index(x, y)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] > 9:
                cou_p1 += 1
                matrix[x][y] = 0
print("Solution Part1 ->" + str(cou_p1))

# Part 2
matrix = []
for x in range(len(data_input)):
    matrix.append([])
    for y in data_input[x]:
        matrix[x].append(int(y))
found = False
cou_p2 = 0
while not found:
    cou_p2 += 1
    flashed_indexes = []
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            matrix[x][y] += 1
            check_index(x, y)
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] > 9:
                cou_p1 += 1
                matrix[x][y] = 0
    zero_cou = 0
    for x in matrix:
        zero_cou += x.count(0)
    if zero_cou == 100:
        found = True
        print("Solution Part2 -> " + str(cou_p2))
