#! /usr/bin/env python

import os
file_dir = "../class_data/"
file_name_servers = "servers.txt"
file_name_updates = "serverupdates.txt"
file_name_no_updates = "servers_no_updates.txt"
total_characters = 0
total_letters = 0
uppercase_letters = range(65, 91)
lowercase_letters = range(97, 123)


def read_file_to_set(fn):
    with open(os.path.expanduser(file_dir + fn), 'r') as f:
        return set([i.strip() for i in f.readlines()])


servers = read_file_to_set(file_name_servers)
updates = read_file_to_set(file_name_updates)

if updates.issubset(servers):
    print(f'All updates already contained in server list.')
else:
    missing = updates.difference(servers)
    print(f'{len(missing)} updates are missing in server list: {missing}')
    new_updates = updates - missing

no_updates = servers - updates
print(f'There are {len(missing)} updates that are actually additions: {missing}')
print(f'There are {len(no_updates)} servers without updates: {no_updates}')
print(f'There are {len(new_updates)} servers to update: {new_updates}')

# Use list comprehension to append a newline to each item in the no_updates set
# as we stripped them on reading each line item initially
with open(os.path.expanduser(file_dir + file_name_no_updates), 'w') as f:
    f.writelines([s + '\n' for s in no_updates])
