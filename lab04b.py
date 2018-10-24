#! /usr/bin/env python

import os
from datetime import datetime, date
from pprint import pprint

file_dir = "../class_data/"
file_name = "tmpprecip2012.dat"
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

for year in temp_precip_data:
    print(f'  Month  ', end=' ')
    print(f'Totprec', end = ' ')
    print(f'P. days', end = ' ')
    print(f'Ave hi', end = ' ')
    print(f'Max hi', end = ' ')
    print(f'Min hi')
    for m in range(12):
        precip = [p for p in temp_precip_data[year]['p'][m] if p is not None]
        temp = [t for t in temp_precip_data[year]['t'][m] if t is not None]
        # print(precip)
        # print(temp)

        print(f'{year} - {m + 1:>2d}', end=' ')
        print(f'{sum(precip):>6.2f} ', end = ' ')
        print(f'{len(precip) - precip.count(0):>4d} ', end = ' ')
        print(f'{sum(temp)/len(temp):>7.2f}', end = ' ')
        print(f'{max(temp):>5d} ', end = ' ')
        print(f'{min(temp):>4d} ')
        # print(f'Total Precipitation:      {sum(precip):>6.2f} ', end = ' ')
        # print(f'Average high temperature: {sum(temp)/len(temp):>6.2f}', end = ' ')
        # print(f'Maximum high temperature: {max(temp):>3d} ', end = ' ')
        # print(f'Minimum high temperature: {min(temp):>3d} ')

    # pprint(temp_precip_data)
#             temp_precip_data[year]
#             temp_precip_data[-1] = 12 * []
#         year_index = temp_precip_data.index(year)
#         if month not in temp_precip_data[year_index]:
#             temp_precip_data[year_index].append(month)
#             temp_precip_data[year_index][-1] = []
#         month_index = temp_precip_data[year_index].index(month)
#         if day not in temp_precip_data[year_index][month_index]:
#             temp_precip_data[year_index][month_index].append(day)
#             temp_precip_data[year_index][month_index][-1] = []
#         day_index = temp_precip_data[year_index][month_index].index(day)
#         if high_temp > max_high_temp:
#             max_high_temp = high_temp
#             max_high_temp_day = day_of_year
#         if high_temp < min_high_temp:
#             min_high_temp = high_temp
#             min_high_temp_day = day_of_year
#         if precip > 0:
#             precip_total += precip
#             precip_days += 1
#             if precip > max_precip:
#                 max_precip = precip
#                 max_precip_day = day_of_year
#
# print('\n')
# print(f'Total precipitation: {precip_total:.2f} across {precip_days} days')
# print(f'Max. precipitation: {max_precip:.2f} on {max_precip_day.isoformat()}')
# print(f'Max. temperature in year: {max_high_temp:.0f} on {max_high_temp_day.isoformat()}')
# print(f'Min. temperature in year: {min_high_temp:.0f} on {min_high_temp_day.isoformat()}')
# print('\n')



