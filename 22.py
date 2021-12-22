import re

with open("inputs\\input202122.txt") as f:
    data_input = f.read().split("\n")
data_p1 = data_input[:20]
data_p2 = data_input[20:]
pattern = "([a-z]+) x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)"

# Part 1
on_list = []
for k in data_p1:
    match = re.search(pattern, k)
    switch = match.group(1)
    x_low = min(int(match.group(2)), int(match.group(3))) + 50
    x_high = max(int(match.group(2)), int(match.group(3))) + 50
    y_low = min(int(match.group(4)), int(match.group(5))) + 50
    y_high = max(int(match.group(4)), int(match.group(5))) + 50
    z_low = min(int(match.group(6)), int(match.group(7))) + 50
    z_high = max(int(match.group(6)), int(match.group(7))) + 50
    off_list = []
    for x in range(x_low, x_high+1):
        for y in range(y_low, y_high+1):
            for z in range(z_low, z_high+1):
                if switch == "on":
                    on_list.append((x, y, z))
                if switch == "off":
                    off_list.append((x, y, z))
    on_list = list(set(on_list)-set(off_list))
print(f"Solution Part1 -> {len(on_list)}")
