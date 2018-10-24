#! /usr/bin/env python

from random import randint

num_rolls = 100000
accum_rolls = 11 * [0]


def roll_dice():
    # return randint(1, 6) + randint(1, 6)
    return randint(0, 5) + randint(0, 5)


for roll in range(num_rolls):
    # # x = roll_dice() - 2
    # x = roll_dice()
    # accum_rolls[x] += 1
    accum_rolls[roll_dice()] += 1

print('\n')
for i in range(2, 13):
    print(f'{i:>2}\t{accum_rolls[i - 2]:>10}\t{accum_rolls[i - 2]/num_rolls:> 8.2%}')