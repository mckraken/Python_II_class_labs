#! /usr/bin/env python

import os

from datetime import datetime, time, date

file_dir = "~/training/ru-python/python_02/class_data/"
file_name = "tmpprecip2012.dat"
full_file_w_path = file_dir + file_name
precip_days = 0
max_precip = 0
precip_total = 0
max_high_temp = -10000000
min_high_temp = 10000000

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
        if high_temp > max_high_temp:
            max_high_temp = high_temp
            max_high_temp_day = day_of_year
        if high_temp < min_high_temp:
            min_high_temp = high_temp
            min_high_temp_day = day_of_year
        if precip > 0:
            precip_total += precip
            precip_days +=1
            if precip > max_precip:
                max_precip = precip
                max_precip_day = day_of_year

print('\n')
print(f'Total precipitation: {precip_total:.2f} across {precip_days} days')
print(f'Max. precipitation: {max_precip:.2f} on {max_precip_day.isoformat()}')
print(f'Max. temperature in year: {max_high_temp:.0f} on {max_high_temp_day.isoformat()}')
print(f'Min. temperature in year: {min_high_temp:.0f} on {min_high_temp_day.isoformat()}')
print('\n')