a_pos = 2
a_score = 0
b_pos = 1
b_score = 0
rolls = [x for x in range(1, 101)]
rolls_cou = 0

# Part 1
while not (a_score >= 1000 or b_score >= 1000):
    dice_val = 0
    for _ in range(3):
        dice_val += rolls[rolls_cou % 100]
        rolls_cou += 1
    if rolls_cou % 2 == 1:
        a_pos = (a_pos + (dice_val % 10)) % 10
        if a_pos == 0:
            a_pos = 10
        a_score += a_pos
    else:
        b_pos = (b_pos + (dice_val % 10)) % 10
        if b_pos == 0:
            b_pos = 10
        b_score += b_pos
if a_score < 1000:
    print(f"Solution Part1 -> {a_score * rolls_cou}")
else:
    print(f"Solution Part1 -> {b_score * rolls_cou}")
