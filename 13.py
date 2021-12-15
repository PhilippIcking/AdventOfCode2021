import re
with open("inputs\\input202113.txt") as f:
    data_input = f.read().split("\n")
points = data_input[:840]
steps = data_input[841:]
coor = []
for x in points:
    k = x.split(",")
    coor.append((int(k[0]), int(k[1])))
paper = [["." for x in range(max(x for x, _ in coor) + 1)] for y in range(max(y for _, y in coor) + 1)]
for x in coor:
    paper[x[1]][x[0]] = "#"


def fold_y(y_coor, paper):
    for y in range(y_coor + 1, len(paper)):
        for x in range(len(paper[0])):
            if paper[y][x] == "#":
                paper[int(2 * y_coor) - y][x] = "#"
    paper = paper[:y_coor]
    return paper


def fold_x(x_coor, paper):
    for y in range(len(paper)):
        for x in range(x_coor + 1, len(paper[0])):
            if paper[y][x] == "#":
                paper[y][int(2 * x_coor) - x] = "#"
    for y in range(len(paper)):
        paper[y] = paper[y][:x_coor]
    return paper


pattern = "fold along ([a-z])=([0-9]+)"
for x in steps:
    match = re.search(pattern, x)
    if str(match.group(1)) == "x":
        paper = fold_x(int(match.group(2)), paper)
    elif str(match.group(1)) == "y":
        paper = fold_y(int(match.group(2)), paper)

for x in paper:
    print(x)
