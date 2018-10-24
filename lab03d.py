#! /usr/bin/env python

from random import randint

# birthday_list = list()
num_dups = list()

num_trys = 100000
num_paradox = 23

for n in range(0, num_trys):
    birthday_list = list()
    for i in range(0, num_paradox):
        birthday_list.append(randint(1, 365))

    y = 0
    for i in range(len(birthday_list)):
        x = birthday_list.pop()
        y += birthday_list.count(x)

    num_dups.append(y)

count = len(num_dups) - num_dups.count(0)

print('\n')
print(f'Maximum number of duplicates found: {max(num_dups)}')
print(f'{count} times duplicates found out of {num_trys} samples (average; {count/num_trys:.2%})')
