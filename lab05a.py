#! /usr/bin/env python

"""Temperature Conversion

This program converts one temperature from fahrenheit to centigrade
(in a void or fruitless function) and prints the results.
Change it to handle a variable number of temperatures to covert and
print in the function.
"""

def fahrenheit_to_centigrade(*args):
    for fdeg in [a for a in args if isinstance(a, (int, float))]:
        cdeg = 5 / 9 * (fdeg - 32)
        print(f'{fdeg:>7.1f} degrees Fahrenheit is {cdeg:>7.1f} degrees Centigrade')


temp = 72
fahrenheit_to_centigrade(temp)
fahrenheit_to_centigrade(88, 72, -10.5, 'a', 111, 55, 45, 95)
