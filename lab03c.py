#! /usr/bin/env python

import os

file_dir = "../class_data/"
file_name = "trees.dat"
full_file_w_path = file_dir + file_name
tree_heights = list()

with open(os.path.expanduser(full_file_w_path), 'r') as f:

    for line in f:
        try:
            tree_heights.append(int(line))
        except ValueError:
            print(f'{line!r} - Bad Data')
            continue

num_trees = len(tree_heights)
ave_height_trees = sum(tree_heights)/len(tree_heights)
max_height_trees = max(tree_heights)
min_height_trees = min(tree_heights)

print('\n')
print(f'Total number of trees measured:   {num_trees:>4d}')
print(f'Average height of trees measured: {ave_height_trees:7.2f}')
print(f'Maximum height of trees measured: {max_height_trees:>4d}')
print(f'Minimum height of trees measured: {min_height_trees:>4d}')
print('\n')
