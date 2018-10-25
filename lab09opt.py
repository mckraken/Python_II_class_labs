#! /usr/bin/env python

import os
from datetime import date

file_dir = "../class_data/"
# file_name = "tmpprecip2012.dat"
file_name = "tmpprecip.dat"
full_file_w_path = file_dir + file_name
precip_days = 0
max_precip = 0
precip_total = 0
max_high_temp = -10000000
min_high_temp = 10000000

temp_precip_data = dict()
with open(os.path.expanduser(full_file_w_path), 'r') as f:

    for line in f:
        try:
            month = int(line[0:2])
            day = int(line[2:4])
            year = int(line[4:8])
            precip = float(line[8:13])
            high_temp = int(line[13:])
            day_of_year = date(year, month, day)
        except ValueError:
            print(f'{line!r} - Bad Data')
            continue
        if year not in temp_precip_data:
            temp_precip_data[year] = dict()
            temp_precip_data[year]['t'] = 12 * [0]
            temp_precip_data[year]['p'] = 12 * [0]
            for m in range(12):
                temp_precip_data[year]['t'][m] = 31 * [None]
                temp_precip_data[year]['p'][m] = 31 * [None]

        temp_precip_data[year]['t'][month - 1][day - 1] = high_temp
        temp_precip_data[year]['p'][month - 1][day - 1] = precip

for year in sorted(temp_precip_data):
    print()
    print(f' Month  ', end=' ')
    print(f'P.Tot ', end=' ')
    print(f'P.days', end=' ')
    print(f'Ave hi', end=' ')
    print(f'Max hi', end=' ')
    print(f'Min hi')
    print(f'{"============================================":^44s}')
    year_temp = []
    year_prec = []
    for m in range(12):
        precip = [p for p in temp_precip_data[year]['p'][m] if p is not None]
        temp = [t for t in temp_precip_data[year]['t'][m] if t is not None]

        print(f'{year}-{m + 1:0>2d}', end=' ')
        print(f'{sum(precip):>6.2f} ', end=' ')
        print(f'{len(precip) - precip.count(0):>4d} ', end=' ')
        print(f'{sum(temp)/len(temp):>7.2f}', end=' ')
        print(f'{max(temp):>5d} ', end=' ')
        print(f'{min(temp):>4d} ')

        year_prec.extend(precip)
        year_temp.extend(temp)

    print(f'{"--------------------------------------------":^44s}')
    print(f'{year:^7d}', end=' ')
    print(f'{sum(year_prec):>6.2f} ', end=' ')
    print(f'{len(year_prec) - year_prec.count(0):>4d} ', end=' ')
    print(f'{sum(year_temp)/len(year_temp):>7.2f}', end=' ')
    print(f'{max(year_temp):>5d} ', end=' ')
    print(f'{min(year_temp):>4d} ')
