#! /usr/bin/env python

from random import randint

num_dups = list()

num_trys = 100000
num_paradox = 23

for n in range(0, num_trys):
    birthday_list = list()
    for i in range(0, num_paradox):
        birthday_list.append(randint(1, 365))

    birthday_set = set(birthday_list)
    num_dups.append(len(birthday_list) - len(birthday_set))

count = len([x for x in num_dups if x > 0])

print('\n')
print(f'Maximum number of duplicates found: {max(num_dups)}')
print(f'{count} times duplicates found out of {num_trys} samples'
      f' (average; {count/num_trys:.2%})')
