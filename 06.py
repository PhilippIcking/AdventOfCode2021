import math
with open("inputs\\input202106.txt") as f:
    data_input = f.read().split(",")


def howmanyseals(max_days):         #O(n^2)
    seals = []
    for x in data_input:
        seals.append(int(x))
    days = 0
    while days < max_days:
        for x in range(len(seals)):
            if seals[x] == 0:
                seals[x] = 6
                seals.append(8)
            else:
                seals[x] = seals[x] - 1
        days += 1
    return len(seals)


print("Solution Part1 -> " + str(howmanyseals(80)))
#print("Solution Part2 -> " + str(howmanyseals(256)))

