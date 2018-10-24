#! /usr/bin/env python

import os
import string

alice_file_dir = "~/training/ru-python/python_02/class_data/"
alice_file = "alice_in_wonderland.dat"
full_file_w_path = alice_file_dir + alice_file

words = {"gryphon", "caterpillar"}

with open(os.path.expanduser(full_file_w_path), 'r') as f:

    book = f.read().lower()
    for word in words:
        print('\n')
        print(f'first occurance of {word} or {word.title()}: {book.find(word)}')
        print(f'last occurance of {word} or {word.title()}: {book.rfind(word)}')
        print(f'number of occurances of {word} or {word.title()}: {book.count(word)}')
print('\n')


