#! /usr/bin/env python

from random import randint

num_rolls = 100000
accum_rolls = 12 * [0]

def roll_dice():
    roll = randint(1, 6) + randint(1, 6)
    print(roll, end=" ")
    return roll

cash = max_cash = 100
turns = 0
while cash > 0:
    if cash > max_cash:
        max_cash = cash
    turns += 1
    x = roll_dice()
    if x in {7, 11}:
        cash += 10
        print(f"\nYou win!! Cash = ${cash}!")
    elif x in {2, 3, 12}:
        cash -= 10
        print(f"\nYou lose! Cash = ${cash}!")
        continue
    else:
        while True:
            y = roll_dice()
            if y == 7:
                cash -= 10
                print(f"\nYou lose! Cash = ${cash}!")
                break
            if y == x:
                cash += 10
                print(f"\nYou win!! Cash = ${cash}!")
                break
print(f'It took {turns} turns to run out of money.  The maximum cash you had was: ${max_cash}')