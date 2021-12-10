with open("inputs\\input202110.txt") as f:
    data_input = f.read().split("\n")

# Part 1 and Part 2
cou_p1 = 0
p2_list = []
for x in data_input:
    poss_char = []
    found = False
    for y in x:
        if not found:
            if y == "(":
                poss_char.append(")")
            elif y == "[":
                poss_char.append("]")
            elif y == "{":
                poss_char.append("}")
            elif y == "<":
                poss_char.append(">")
            else:
                if y == poss_char[-1]:
                    poss_char.__delitem__(-1)

                else:
                    if y == ")":
                        cou_p1 += 3
                        found = True
                    elif y == "]":
                        cou_p1 += 57
                        found = True
                    elif y == "}":
                        cou_p1 += 1197
                        found = True
                    elif y == ">":
                        cou_p1 += 25137
                        found = True
    if len(poss_char) != 0 and not found:
        akt_cou = 0
        for c in range(1, len(poss_char)+1):
            akt_cou *= 5
            if poss_char[-c] == ")":
                akt_cou += 1
            elif poss_char[-c] == "]":
                akt_cou += 2
            elif poss_char[-c] == "}":
                akt_cou += 3
            elif poss_char[-c] == ">":
                akt_cou += 4
        p2_list.append(akt_cou)
print("Solution Part1 -> " + str(cou_p1))
p2_list = sorted(p2_list)
print("Solution Part2 -> " + str(p2_list[int(len(p2_list)/2)]))
