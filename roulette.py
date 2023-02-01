import random
import matplotlib.pyplot as plt

# bet $1 initally and double the bet whenever the player loses and reset the bet to $1 when the player wins.
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

# same strategy as in martingale(), but resetting the bet to $1 once a $512 bet is lost
def martingale_b(n_games):
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
            if (bet == 512):
                bet = 1
            else:
                bet *= 2
        profits_history.append(profit)
    
    return profits_history

# same strategy as in martingale(), but keep betting $1000 once once a $512 bet is lost
def martingale_c(n_games):
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


martingale = martingale_b(1000)
plt.plot(martingale, linewidth=1)
plt.xlabel("Number of Games", fontsize=10)
plt.ylabel("Profits", fontsize=10)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.title("Cumulative Profits", fontsize=10)
plt.show()
