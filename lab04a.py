#! /usr/bin/env python
"""
Stacks and Queues
"""
from random import randrange
from datetime import datetime
from collections import deque

num_items = 5

stack = []
for i in range(0, num_items):
    stack.append(randrange(0, 100))
    print(stack)

while len(stack) > 0:
    print(f'Using: {stack.pop()}, leaving stack as: {stack}')

# Option A as instructor requested
queue = []
for i in range(0, num_items):
    queue.insert(0, randrange(0, 100))
    print(queue)

while len(queue) > 0:
    print(f'Using {queue.pop()}, leaving stack as: {queue}')

# Option B
queue = []
for i in range(0, num_items):
    queue.append(randrange(0, 100))
    print(queue)

while len(queue) > 0:
    print(f'Using {queue.pop(0)}, leaving stack as: {queue}')

# Option C
queue = deque([])
for i in range(0, num_items):
    queue.append(randrange(0, 100))
    print(queue)

while len(queue) > 0:
    print(f'Using {queue.popleft()}, leaving stack as: {queue}')
