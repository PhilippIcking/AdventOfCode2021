with open("inputs\\input202114.txt") as f:
    data_input = f.read().split("\n")
print(data_input)
polymer_template = data_input[0]
insertion_list = data_input[2:]


def checkpair(pair):
    for y in insertion_list:
        if y[:2] == pair:
            return y[-1]
    pass


for i in range(10):
    akt_template = ""
    for x in range(len(polymer_template) - 1):
        akt_pair = polymer_template[x:x + 2]
        letter_ins = checkpair(akt_pair)
        akt_template = akt_template.__add__(akt_pair[0])
        akt_template = akt_template.__add__(letter_ins)
    akt_template = akt_template.__add__(akt_pair[1])
    polymer_template = akt_template
highest = 0
lowest = 100000000
ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in ABC:
    if polymer_template.count(x) > highest:
        highest = polymer_template.count(x)
    if polymer_template.count(x) < lowest and polymer_template.count(x) != 0:
        lowest = polymer_template.count(x)
print("Solution Part1 -> " + str(highest-lowest))
