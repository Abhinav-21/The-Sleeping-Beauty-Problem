
# Sleeping Beauty volunteers to undergo the following experiment and is told all of the following details: 
# On Sunday she will be put to sleep. Once or twice, during the experiment, Sleeping Beauty will be 
# awakened, interviewed, and put back to sleep with an amnesia-inducing drug that makes her forget 
# that awakening. A fair coin will be tossed to determine which experimental procedure to undertake:

#? 1. If the coin comes up heads, Sleeping Beauty will be awakened and interviewed on Monday only.
#? 2. If the coin comes up tails, she will be awakened and interviewed on Monday and Tuesday.
#? 3. In either case, she will be awakened on Wednesday without interview and the experiment ends.

# Any time Sleeping Beauty is awakened and interviewed she will not be able to tell which day it is
# or whether she has been awakened before. During the interview Sleeping Beauty is asked: 

#! "What is your credence now for the proposition that the coin landed heads?"


import random as rd

choice = 0.5
correct = 0
total = 0
coin = ["heads", "tails"]
coins = ["heads", "tails", "tails"]
for i in range(10000000):
    result = rd.choices(coin)[0]
    x = rd.choices(coins)[0]
    if x == "heads" and result == "heads":
        correct += 1
        total += 1
        
    elif x == "heads" and result == "tails":
        total += 1
        x = rd.choices(coins)[0]
        if x == "tails":
            correct += 1
            total += 1
        else:
            total += 1
            
    elif x == "tails" and result == "tails":
        correct += 1
        total += 1
        x = rd.choices(coins)[0]
        if x == "tails":
            correct += 1
            total += 1
        else:
            total += 1
        
    elif x == "tails" and result == "heads":
        total += 1
        

print(round(100*correct/total, 2), "%", sep="")
