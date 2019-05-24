# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import numpy as np


# def pythagorean_triplet(res):
#     for a in range(1, 1001):
#         for b in range(1, 1001):
#             for c in range(1, 1001):
#                 print(str(a), ' ', str(b), ' ', str(c))
#                 if a < b < c:
#                     product = a ** 2 + b ** 2
#                     if product == c ** 2 and a + b + c == res:
#                         return a, b, c

#
# print(pythagorean_triplet(1000))

# Generating from (a,b,c)=(3,4,5)M


def gen_prim_pyth_trips(limit=None):
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)


def gen_all_pyth_trips(limit):
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit//prim[2]):
            yield i
            i = i + prim