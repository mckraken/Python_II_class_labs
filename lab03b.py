#! /usr/bin/env python

from functools import reduce

mylist = list(range(2, 18, 3))
print(mylist)

ev_mylist = [x for x in mylist if x % 2 == 0]
print(ev_mylist)
ev_mylist = list(filter(lambda x: x % 2 == 0, mylist))
print(ev_mylist)
sq_mylist = list(map(lambda x: x**2, mylist))
print(sq_mylist)
sq_mylist = [x**2 for x in mylist]
print(sq_mylist)
sum_mylist = reduce((lambda x, y: x+y), mylist)
print(sum_mylist)
sum_mylist = sum(mylist)
print(sum_mylist)
