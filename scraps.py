import random
import numpy as np


def check_score(point):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    score = die1 + die2
    return score == point

def roll_two_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2



win = 0
fixed = 0
points = [4, 5, 6, 8, 9, 10]

n_simulations = 1000000

for i in range(n_simulations):

    if check_score(7) or check_score(11):
        win += 1
        continue

    point = roll_two_dice()

    if point in points:
        for i in range(100000):
            if check_score(point):
                win += 1
                break
            i += 1

print(win/n_simulations)
