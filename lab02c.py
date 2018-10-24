#! /usr/bin/env python

import os
import string

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

for ch in string.printable:
    if ch in letter_count:
        print(f'Occurances of {ch!r:>4} (ascii {ord(ch):>3}): {letter_count[ch]:>5}\t{letter_count[ch]/total_characters:8.2%}')
    # else:
    #     print(f'{ch!r} not found in file.')
