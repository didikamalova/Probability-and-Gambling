
import random
from random import randint
from random import sample
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Generalized Monty Hall Problem

# This function will generate random rounds with n doors for our game and keep them in a list.
def generate_game(n_games, n_doors):
    game = []

    for i in range(n_games):
        doors = [False] * n_doors
        winner = randint(0, n_doors-1)
        doors[winner] = True
        game.append(doors)

    return game

# This is a helper function that takes a list of n doors, an index of a chosen door and chooses n-2 the door(s) with the goat among the remaining ones.
def reveal_goat(doors, chosen):
    n_doors = len(doors)

    if doors[chosen] == True:
        return sample([i for i in range(n_doors) if i != chosen], n_doors - 2)
        # have to deal with orders od indices here!!!
    elif doors[chosen] == False:
        return [i for i in range(n_doors) if (i != chosen and doors[i] != True)]


def simulate_keep_choice(game):
    wins = 0
    attempts = 0
    history = []

    for doors in game:
        attempts += 1
        
        chosen = random.randrange(n_doors)
        if (doors[chosen] == True):
            wins += 1

        history.append(wins / attempts)

    return wins, history

def simulate_switch_choice(game):
    wins = 0
    attempts = 0
    history = []

    for doors in game:
        attempts += 1
        chosen = random.randrange(n_doors)

        goat = reveal_goat(doors, chosen)
        new_choice = [i for i in range(n_doors) if(i not in goat and i != chosen)]

        if (doors[new_choice[0]] == True):
            wins += 1
            
        history.append(wins / attempts)

    return wins, history

# Beginning computation

n_games = 1000
n_doors = 5
game = generate_game(n_games, n_doors)

wins_keep, history_keep = simulate_keep_choice(game)
print('keep ', wins_keep/n_games)

wins_switch, history_switch = simulate_switch_choice(game)
print('switch', wins_switch/n_games)

plt.figure(figsize=(12,8))
plt.plot(history_keep, 'g', label="Keep initial")
plt.plot(history_switch, 'b', label="Only switch")
plt.legend(loc='upper right')
plt.ylim(0, 1.0)
plt.xlim(0, 1000)
plt.ylabel("Chance", fontsize=16)
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1.0)) 
plt.xlabel("Iterations", fontsize=16)
plt.grid(True)
plt.show()