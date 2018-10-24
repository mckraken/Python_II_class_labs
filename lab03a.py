#! /usr/bin/env python

from random import randint

num_rolls = 100000
accum_rolls = 11 * [0]


def roll_dice():
    return randint(0, 5) + randint(0, 5)


for roll in range(num_rolls):
    accum_rolls[roll_dice()] += 1

print('\n')
for i in range(0, 11):
    print(f'{i + 2:>2}\t{accum_rolls[i]:>10}\t{accum_rolls[i]/num_rolls:> 8.2%}')
