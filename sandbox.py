import logging
import numpy as np
from pprint import pprint
from sys import stdout as STDOUT 


# def my_coroutine():
#     while True:
#         received = yield
#         print('Received:', received)

# it = my_coroutine()
# next(it)
# it.send('First')
# it.send('second')

def minimize():
    current = float("inf") 
    # current = yield
    print("current")
    while True:
        value = yield current
        current = min(value, current)

it = minimize()
next(it) # current = yield が実行
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))

# ALIVE='*'
# EMPTY='-'

# from collections import namedtuple
# que = namedtuple('Query',('y', 'x'))

# def count_neighbors(y, x):
#     n_ = yield que(y + 1, x + 0)
#     ne = yield que(y + 1, x + 1)
#     e_ = yield que(y + 0, x + 1)
#     se = yield que(y - 1, x + 1)
#     s_ = yield que(y - 1, x + 0)
#     sw = yield que(y - 1, x - 1)
#     w_ = yield que(y + 0, x - 1)
#     nw = yield que(y + 1, x - 1)
#     neighbor_states = [ n_ , ne , e_ , se, s_, sw, w_, nw ]
#     print ( neighbor_states)
#     count = 0
#     for state in neighbor_states:
#         if state == ALIVE:
#             count += 1
#     return count

# it = count_neighbors(10, 5)
# q1 = next(it)
# print("first yield:", q1)
# q2 = it.send(ALIVE)            # Send q1 state, get q2
# print('Second yield:', q2)
# q3 = it.send(ALIVE)            # Send q2 state, get q3
# print('...')
# q4 = it.send(EMPTY)
# q5 = it.send(EMPTY)
# q6 = it.send(EMPTY)
# q7 = it.send(EMPTY)
# q8 = it.send(EMPTY)
# try:
#     it.send(EMPTY)     # Send q8 state, retrieve count
# except StopIteration as e:
#     print('Count: ', e.value)  # Value from return statement
