#! /usr/bin/env python

"""Temperature Conversion

This program converts one temperature from fahrenheit to centigrade
(in a void or fruitless function) and prints the results.
Change it to handle a variable number of temperatures to covert and
print in the function.
"""

from sys import argv, stderr


def fahrenheit_to_centigrade(*args):
    # for fdeg in [float(a) for a in args if str(a).isnumeric()]:
    for item in args:
        try:
            fdeg = float(item)
        except ValueError:
            print(f'{item} ({type(item)}) is not valid for conversion',
                  file=stderr)
            continue

        cdeg = 5 / 9 * (float(fdeg) - 32)
        print(f'{float(fdeg):>7.1f} degrees Fahrenheit is '
              f'{cdeg:>7.1f} degrees Centigrade')


fahrenheit_to_centigrade(*argv[1:])