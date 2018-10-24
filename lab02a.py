#! /usr/bin/env python

import os
file_dir = "../class_data/"
file_name = "alice_in_wonderland.dat"
full_file_w_path = file_dir + file_name
total_characters = 0
total_letters = 0
uppercase_letters = range(65, 91)
lowercase_letters = range(97, 123)

with open(os.path.expanduser(full_file_w_path), 'r') as f:

    letter_count = dict()
    for line in f:
        for char in line:
            key = str(ord(char))
            total_characters += 1
            if ord(char) in uppercase_letters or ord(char) in lowercase_letters:
                total_letters += 1
            if key in letter_count:
                letter_count[key] += 1
            else:
                letter_count[key] = 1

print(f'Occurances of "e" {letter_count[str(ord("e"))]}')
print(f'Occurances of "E" {letter_count[str(ord("E"))]}')
case_insensitive_e = letter_count[str(ord("E"))] + letter_count[str(ord("e"))]
print(f'Total "e" and "E" {case_insensitive_e}')
print(f'Total Characters {total_characters}')
print(f'Total Letters {total_letters}')
print(f'case insensitive "e" percentage of characters: {case_insensitive_e/total_characters:.2%}')
print(f'case insensitive "e" percentage of letters {case_insensitive_e/total_letters:.2%}')
