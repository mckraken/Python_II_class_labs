#! /usr/bin/env python

import os
from operator import itemgetter

file_dir = "../class_data/"
gdp_file = "gdp.txt"

fn = gdp_file
gdp_lst = []
with open(os.path.expanduser(file_dir + fn), 'r') as f:
    for line in f:
        gdp_lst.append(line.strip().split(','))

for country_data in gdp_lst:
    country_data.append(round(int(country_data[1]) * 1000000/int(country_data[2]), 2))

print('\n')
print(f'{"Country data sorted by GDP per capita":^46s}')
print(f'{"=====================================":^46s}')
print(f'{"Country":>20s} - {"GDP/capita":^10s}')
for item in sorted(gdp_lst, key=itemgetter(3), reverse=True):
    print(f'{item[0]:>20} | ${item[3]:>9.2f}')


