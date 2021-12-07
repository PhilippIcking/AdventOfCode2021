with open("inputs\\input202104.txt") as f:
    data_input = f.read().split("\n\n")
rand_numbs = data_input[0].split(",")
for x in range(len(rand_numbs)):
    rand_numbs[x] = int(rand_numbs[x])

mat_raw = []
for x in data_input[1:]:
    mat_raw.append(x.split("\n"))
mat = []
for x in range(len(mat_raw)):
    for y in range(len(mat_raw[x])):
        mat_raw[x][y] = mat_raw[x][y].replace("  ", " ")
        mat_raw[x][y] = mat_raw[x][y].removeprefix(" ")
        mat.append(mat_raw[x][y].split(" "))
for x in range(len(mat)):
    for y in range(len(mat[x])):
        mat[x][y] = int(mat[x][y])

matrix = []
all_matrix = []
for x in range(len(mat)):
    matrix.append(mat[x])
    if x % 5 == 4:
        all_matrix.append(matrix)
        matrix = []


def won(akt_matrix):
    for j in range(5):
        if akt_matrix[j].count("x") == 5:
            return True
        cou = 0
        for k in range(5):
            if akt_matrix[k][j] == "x":
                cou += 1
        if cou == 5:
            return True
    else:
        return False


def matrix_sum(akt_matrix):
    cou = 0
    for k in range(5):
        for l in range(5):
            if akt_matrix[k][l] != "x":
                cou += akt_matrix[k][l]
    return cou


# Part 1 and 2
won_boards = []
score = []
for a in rand_numbs:
    for x in range(len(all_matrix)):
        for y in range(5):
            for z in range(5):
                if a == all_matrix[x][y][z]:
                    all_matrix[x][y][z] = "x"
        if won(all_matrix[x]):
            if won_boards.count(x) == 0:
                won_boards.append(x)
                score.append(a * matrix_sum(all_matrix[x]))
            if len(won_boards) == 100:
                print("Solution Part1 -> " + "Board: " + str(won_boards[0]) + " with " + str(score[0]) + " Points")
                print("Solution Part2 -> " + "Board: " + str(won_boards[-1]) + " with " + str(score[-1]) + " Points")
                exit()
