import random
from random import randint
from random import sample
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def martingale(n_games):
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    profit = 0
    bet = 1
    profits_history = []

    for i in range(n_games):
        roll = random.choice(pockets)
        if roll == "Red":
            profit += bet
            bet = 1
        else:
            profit -= bet
            bet *= 2
        profits_history.append(profit)
    
    return profits_history

def martingale_limited(n_games):
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    profit = 0
    bet = 1
    profits_history = []

    for i in range(n_games):
        roll = random.choice(pockets)
        if roll == "Red":
            profit += bet
            bet = 1
        else:
            profit -= bet
            if (bet*2 == 1024):
                bet = 1
            else:
                bet *= 2
        profits_history.append(profit)
    
    return profits_history

def martingale_3(n_games):
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    profit = 0
    bet = 1
    profits_history = []

    for i in range(n_games):
        roll = random.choice(pockets)
        if roll == "Red":
            profit += bet
            if (bet % 1000 == 0):
                bet = 1000
            else:
                bet = 1
        else:
            profit -= bet
            if (bet*2 == 1024):
                bet = 1000
            elif (bet % 1000 == 0):
                bet = 1000
            else:
                bet *= 2
        profits_history.append(profit)
    
    return profits_history


martingale = martingale(1000000)
plt.plot(martingale, linewidth=2)
plt.xlabel("Number of Games", fontsize=10, fontweight="bold")
plt.ylabel("Profits", fontsize=10, fontweight="bold")
plt.xticks(fontsize=10, fontweight="bold")
plt.yticks(fontsize=10, fontweight="bold")
plt.title("Cumulative Profits", fontsize=10, fontweight="bold")
plt.show()
