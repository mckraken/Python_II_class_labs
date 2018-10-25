#! /usr/bin/env python

"""Temperature Conversion

This program converts one temperature from fahrenheit to centigrade
(in a void or fruitless function) and prints the results.
Change it to handle a variable number of temperatures to covert and
print in the function.
"""

from sys import argv, stderr, exit
from string import whitespace, punctuation


def rotate(*args):
    s = args[0]
    r = int(args[2] + args[1]) % 26
    new = []
    for c in s:
        if c in whitespace:
            new.append(c)
        elif c in punctuation:
            new.append(c)
        elif c == c.lower():
            new.append(chr(((ord(c) - 97 + r) % 26) + 97))
        else:
            new.append(chr(((ord(c) - 65 + r) % 26) + 65))
    return ''.join(new)


if __name__ == '__main__':
    if len(argv) != 3:
        print(f'"{argv[0]}" takes exactly two parameters,\n'
              f'the first being the string to rotate and\n'
              f'the second being an integer for the amount\n'
              f'to shift the characters.',
              file=stderr)
        exit(1)
    elif not argv[1].translate(
            {ord(c): None for c in whitespace + punctuation}
    ).isalpha():
        print(f'"{argv[1]}" is not a valid alphabetic string',
              file=stderr)
        exit(1)
    elif argv[2][0] not in ["-", "+"]:
        argv.append('+')
        if not argv[2].isdecimal():
            print(f'"{argv[2]}" is not a valid number to shift',
                  file=stderr)
            exit(1)
    else:
        argv.append(argv[2][0])
        argv[2] = argv[2][1:]
        if not argv[2].isdecimal():
            print(f'"{argv[3] + argv[2]}" is not a valid number to shift',
                  file=stderr)
            exit(1)

    print(f'Rotated text:\n{rotate(*argv[1:])}')
