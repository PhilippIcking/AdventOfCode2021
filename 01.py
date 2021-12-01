with open("inputs\\input202101.txt") as f:
    zahlen = list(map(int, f.readlines()))

cou = 0
for x in range(0, len(zahlen)-1):  #Part_1
    if zahlen[x+1] > zahlen[x]:
        cou += 1
print(cou)

cou2 = 0
sum_old = 0
for x in range(0, len(zahlen)-2):  #Part_2
    sum_akt = zahlen[x] + zahlen[x+1] + zahlen[x+2]
    if sum_akt > sum_old != 0:
        cou2 += 1
    sum_old = sum_akt
print(cou2)
