import random
import numpy as np

def roll_two_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

win = 0
fixed = 0
points = [4, 5, 6, 8, 9, 10]
win = [7, 11]
lose = [2, 12, 3]
wins = 0


n_simulations = 1000000

for i in range(n_simulations):
    init = roll_two_dice()

    if init in win:
        wins += 1
        continue
    elif init in lose:
        continue

    point = init

    for i in range(100):
        score = roll_two_dice()

        if score == point:
            wins += 1
            break
        elif score == 7:
            break

print(wins/n_simulations)
