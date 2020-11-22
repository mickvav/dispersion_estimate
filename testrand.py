#!/usr/bin/env python3

from random import random
from collections import defaultdict
Nretrs=10000
Nmask=3030
Nnon=2994
# 0-hypothesis test
d=defaultdict(int)
for retr in range(0,Nretrs):
    n1 = 0
    for i in range(0,Nmask):
        v=random()
        if v<0.0195:
            n1 = n1 + 1
    n2 = 0
    for i in range(0,Nnon):
        v=random()
        if v<0.0195:
            n2 = n2 + 1

    d[n2-n1] = d[n2-n1] + 1
# Counting number of experiments in d, that are above 53-42
mt = 0
for n in d:
    if n >= 53-42:
        mt = mt + d[n]
print(f"0-hypothesis P_(n2-n1 >= 11): {mt/Nretrs}")

# 1-hypothesis test
d=defaultdict(int)
for retr in range(0,Nretrs):
    n1 = 0
    for i in range(0,Nmask):
        v=random()
        if v<0.018:
            n1 = n1 + 1
    n2 = 0
    for i in range(0,Nnon):
        v=random()
        if v<0.021:
            n2 = n2 + 1

    d[n2-n1] = d[n2-n1] + 1
# Counting number of experiments in d, that are above 53-42
mt = 0
for n in d:
    if n >= 53-42:
        mt = mt + d[n]
print(f"1-hypothesis P_(n2-n1 >= 11): {mt/Nretrs}")


