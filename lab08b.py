#! /usr/bin/env python

import os
from string import punctuation

file_dir = "../class_data/"
split_file = "split.txt"

fn = split_file
word_lst = set()
num_words = 0
with open(os.path.expanduser(file_dir + fn), 'r') as f:
    for line_w_punct in f:
        # replace punctuation with space character rather than
        # deleting it so "amazon.com" becomes "amazon" and "com"
        # rather than "amazoncom"
        line = line_w_punct.strip().translate(
            {ord(c): ' ' for c in punctuation}).lower()
        words_in_line = line.split()
        num_words += len(words_in_line)
        word_lst.update(words_in_line)

print('\n')
print(f'{"Sorted unique word list in file":^36s}')
print(f' Word count: {num_words} Unique words: {len(word_lst)}')
print(f'{"===========================++++====":^36s}')
for item in sorted(word_lst):
    print(f'  {item:<}  ')
