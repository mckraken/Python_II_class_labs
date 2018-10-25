#! /usr/bin/env python

import os
import string

file_dir = "../class_data/"
file_name = "alice_in_wonderland.dat"
full_file_w_path = file_dir + file_name
total_characters = 0
total_letters = 0
total_whitespace = 0

with open(os.path.expanduser(full_file_w_path), 'r') as f:

    letter_count = dict()
    for line_w_whitespace in f:
        line = line_w_whitespace.translate(
            {ord(c): None for c in string.whitespace}
        ).lower()
        total_whitespace += len(line_w_whitespace) - len(line)
        for char in line:
            key = char
            total_characters += 1
            if char.isalpha():
                total_letters += 1
            letter_count[key] = letter_count.get(key, 0) + 1

sd = [(v, k) for k, v in letter_count.items()]
sd.sort()
# print(sd)
for n in range(30):
    i = sd.pop()
    print(f"Character '{i[1]}' used {i[0]:>6d} "
          f"times ({i[0]/total_characters:>7.2%})")

print('\n')
print(f'Total Characters {total_characters}')
print(f'Total Letters {total_letters}')
print(f'Total Whitespace Characters Removed {total_whitespace}')
