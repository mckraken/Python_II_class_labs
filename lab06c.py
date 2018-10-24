#! /usr/bin/env python

from random import randint

import os
file_dir = "../class_data/"
file_name_servers = "servers.txt"
file_name_updates = "serverupdates.txt"
total_characters = 0
total_letters = 0
uppercase_letters = range(65, 91)
lowercase_letters = range(97, 123)

servers = set()
updates = set()

def read_file_to_set(fn, sn):
    with open(os.path.expanduser(file_dir + fn), 'r') as f:
        for item in f:
            sn.add(item.strip())
    return sn

read_file_to_set(file_name_servers, servers)
read_file_to_set(file_name_updates, updates)

if updates.issubset(servers):
    print(f'All updates already contained in server list.')
else:
    missing = updates.difference(servers)
    print(f'{len(missing)} updates are missing in server list: {missing}')
    new_updates = updates - missing

servers_no_updates = servers - updates
print(len(servers))
print(len(servers_no_updates))
print(len(new_updates))




