with open("inputs\\input202103.txt") as f:
    numbs = f.readlines()

numbs_clean = []
# Part_1
for x in numbs:
    numbs_clean.append(x.removesuffix("\n"))
final_numb = ""
for y in range(0, len(numbs_clean[0])):
    zero_cou = 0
    one_cou = 0
    for z in numbs_clean:
        if z[y] == "1":
            one_cou += 1
        else:
            zero_cou += 1
    if one_cou > zero_cou:
        final_numb = final_numb + "1"
    else:
        final_numb = final_numb + "0"
final_numb2 = ""
for i in range(0, len(final_numb)):
    if final_numb[i] == "1":
        final_numb2 = final_numb2 + "0"
    else:
        final_numb2 = final_numb2 + "1"
print("Solution Part1 -> " + str(int(final_numb, 2) * int(final_numb2, 2)))
# Part_2
found = False
i = 0
numbs_false = []

while not found:
    zero_cou = 0
    one_cou = 0
    numbs_false_one = []
    numbs_false_zero = []
    for x in range(0, len(numbs_clean)):
        if 1 > numbs_false.count(x):
            if numbs_clean[x][i] == "1":
                one_cou += 1
                numbs_false_one.append(x)

            else:
                zero_cou += 1
                numbs_false_zero.append(x)
    if zero_cou > one_cou:
        numbs_false = numbs_false + numbs_false_one
    elif one_cou > zero_cou:
        numbs_false = numbs_false + numbs_false_zero
    else:
        for y in range(0, len(numbs_clean)):
            if 1 > numbs_false.count(y):
                if numbs_clean[y][i] == "1":
                    oxy_gen_rating = int(numbs_clean[y], 2)
                    found = True

    i += 1


found = False
i = 0
numbs_false = []

while not found:
    zero_cou = 0
    one_cou = 0
    numbs_false_one = []
    numbs_false_zero = []
    for x in range(0, len(numbs_clean)):
        if 1 > numbs_false.count(x):
            if numbs_clean[x][i] == "1":
                one_cou += 1
                numbs_false_one.append(x)

            else:
                zero_cou += 1
                numbs_false_zero.append(x)
    if zero_cou > one_cou:
        numbs_false = numbs_false + numbs_false_zero
    elif one_cou > zero_cou:
        numbs_false = numbs_false + numbs_false_one
    else:
        for y in range(0, len(numbs_clean)):
            if 1 > numbs_false.count(y):
                if numbs_clean[y][i] == "0":
                    co_sru_rating = int(numbs_clean[y], 2)
                    found = True

    i += 1

print("Solution Part2 -> " + str(co_sru_rating*oxy_gen_rating))
