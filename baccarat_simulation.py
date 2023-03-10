import numpy as np

drawRules = [[1,1,1,1,0,0,0,0], # player third card 0
             [1,1,1,1,0,0,0,0], # player third card 1
             [1,1,1,1,1,0,0,0], # player third card 2
             [1,1,1,1,1,0,0,0], # player third card 3
             [1,1,1,1,1,1,0,0], # player third card 4
             [1,1,1,1,1,1,0,0], # player third card 5
             [1,1,1,1,1,1,1,0], # player third card 6
             [1,1,1,1,1,1,1,0], # player third card 7
             [1,1,1,0,0,0,0,0], # player third card 8
             [1,1,1,1,0,0,0,0], # player third card 9
            ]

def draw_single():
    return max(np.random.randint(-3,10), 0)

def draw_double():
    return (draw_single() + draw_single()) % 10

# return 1 for player win, 0 for tie, -1 for banker win
def winner(player, banker):
    return np.sign(player - banker)

def game():
    player = draw_single()
    banker = draw_single()

    # natural
    if player > 7 or banker > 7:
        return winner(player, banker)

    # player stands
    if player > 5:
        if banker <= 5:
            banker = (banker + draw_single()) % 10
        return winner(player, banker)
    
    # player draws another card
    player_third = draw_single()
    player = (player + player_third) % 10

    # banker draws a third card according to the rules
    if drawRules[player_third][banker]:
        banker = (banker + draw_single()) % 10
    
    return winner(player, banker)

# Run trai
def run_trials(trials):
    player_wins = 0
    banker_wins = 0
    ties = 0

    for i in range(trials):
        result = game()
        if result == 1: player_wins += 1
        elif result == -1: banker_wins += 1
        else: ties += 1

    print("Player Wins: {}%".format(player_wins/trials*100))
    print("Banker Wins: {}%".format(banker_wins/trials*100))
    print("Ties: {}%".format(ties/trials*100))


run_trials(10000000)