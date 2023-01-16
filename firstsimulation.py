import random
import numpy as np

def roll_the_dice(n_simulations = 100):
    count = 0

    for i in range(n_simulations):

        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        score = die1 + die2
        
        if score % 2 == 0 or score > 7:
            count += 1
        
    return count/n_simulations

string = 'The probability of rolling an even number or greater than 7 is: '
print (string, np.round(roll_the_dice()*100, 2), '%')