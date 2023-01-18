import random
import numpy as np



def roll_two_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

win = 0
fixed = 0
points = [4, 5, 6, 8, 9, 10]


n_simulations = 100

for i in range(n_simulations):
    print('simulation: ', i + 1)

    # first round
    init = roll_two_dice()
    print(init)

    if init == 7 or init == 11:
        win += 1
        continue
    elif init == 3 or init == 2 or init == 12:
        continue
    else:
        point = init

    # subsequent rounds
    for i in range(100):
        score = roll_two_dice()
        if score == point:
            win += 1
            break
        elif score == 7:
            break

print(win/n_simulations)
