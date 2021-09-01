from itertools import count
from math import factorial

def fact(n):
    for element in count(1):
        yield factorial(element)

n = 0
for element in fact(n):
    if n < 8:
        print(element)
        n += 1
    else:
        break