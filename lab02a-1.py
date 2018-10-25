#! /usr/bin/env python

import os
file_dir = "../class_data/"
file_name = "alice_in_wonderland.dat"
full_file_w_path = file_dir + file_name
total_characters = 0
total_letters = 0

with open(os.path.expanduser(full_file_w_path), 'r') as f:

    letter_count = dict()
    for line in f:
        for char in line:
            key = char
            total_characters += 1
            if char.isalpha():
                total_letters += 1
            if key in letter_count:
                letter_count[key] += 1
            else:
                letter_count[key] = 1

print(f'Occurances of "e" {letter_count["e"]}')
print(f'Occurances of "E" {letter_count["E"]}')
case_insensitive_e = letter_count["E"] + letter_count["e"]
print(f'Total "e" and "E" {case_insensitive_e}')
print(f'Total Characters {total_characters}')
print(f'Total Letters {total_letters}')
print(f'case insensitive "e" percentage of characters: '
      f'{case_insensitive_e/total_characters:.2%}')
print(f'case insensitive "e" percentage of letters '
      f'{case_insensitive_e/total_letters:.2%}')
