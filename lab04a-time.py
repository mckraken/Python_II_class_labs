#! /usr/bin/env python
"""
Stacks and Queues
"""
from random import randrange, getrandbits, random
from datetime import datetime
from collections import deque

num_items = 500000

start_loop = datetime.utcnow()
stack = []
for i in range(0, num_items):
    # stack.append(randrange(128))
    stack.append(getrandbits(7))
    # stack.append(random())
    # print(stack)

while len(stack) > 0:
    stack.pop()
    # print(f'Using: {stack.pop()}, leaving stack as: {stack}')
loop_time = datetime.utcnow() - start_loop
print(f'{num_items} iterations of stack append/pop took {loop_time}')

# Option A as instructor requested
start_loop = datetime.utcnow()
queue = []
for i in range(0, num_items):
    # queue.insert(0, randrange(128))
    queue.insert(0, getrandbits(7))
    # queue.insert(0, random())
    # print(queue)

while len(queue) > 0:
    queue.pop()
    # print(f'Using {queue.pop()}, leaving stack as: {queue}')
loop_time = datetime.utcnow() - start_loop
print(f'{num_items} iterations of queue insert/pop took {loop_time}')

# Option B
start_loop = datetime.utcnow()
queue = []
for i in range(0, num_items):
    # queue.append(randrange(128))
    queue.append(getrandbits(7))
    # queue.append(random())
    # print(queue)

while len(queue) > 0:
    queue.pop(0)
    # print(f'Using {queue.pop(0)}, leaving stack as: {queue}')
loop_time = datetime.utcnow() - start_loop
print(f'{num_items} iterations of queue append/pop(0) took {loop_time}')

# Option C
start_loop = datetime.utcnow()
queue = deque([])
for i in range(0, num_items):
    # queue.append(randrange(128))
    queue.append(getrandbits(7))
    # queue.append(random())
    # print(queue)

while len(queue) > 0:
    queue.popleft()
    # print(f'Using {queue.popleft()}, leaving stack as: {queue}')
loop_time = datetime.utcnow() - start_loop
print(f'{num_items} iterations of deque append/popleft took {loop_time}')

getrandbits(7)

# 200000 iterations of stack append/pop took 0:00:00.087298
# 200000 iterations of queue insert/pop took 0:00:08.234231
# 200000 iterations of queue append/pop(0) took 0:00:04.681073
# 200000 iterations of deque append/popleft took 0:00:00.060111
#
# 300000 iterations of stack append/pop took 0:00:00.105176
# 300000 iterations of queue insert/pop took 0:00:19.171572
# 300000 iterations of queue append/pop(0) took 0:00:10.184845
# 300000 iterations of deque append/popleft took 0:00:00.088231
#
# 400000 iterations of stack append/pop took 0:00:00.130791
# 400000 iterations of queue insert/pop took 0:00:36.056219
# 400000 iterations of queue append/pop(0) took 0:00:20.416977
# 400000 iterations of deque append/popleft took 0:00:00.123737
#
# 500000 iterations of stack append/pop took 0:00:00.169068
# 500000 iterations of queue insert/pop took 0:01:01.966784
# 500000 iterations of queue append/pop(0) took 0:00:34.334683
# 500000 iterations of deque append/popleft took 0:00:00.157218
