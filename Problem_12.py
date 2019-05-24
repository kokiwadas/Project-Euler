# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

import math
import time


def div_generator(n):
    large_divisors = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n//i)
    for divisor in reversed(large_divisors):
        yield divisor


def prime_div_generator(n):

    while n % 2 == 0:
        yield n
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            yield n
            n = n / i


def divisors_number(n):
    divisors = yield from div_generator(n)
    return divisors





def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = len(list(divisors_number(n))), len(list(divisors_number(n+1)))

    while lnum * rnum < factor_limit:
        n += 1
        print('lnum: ' + str(lnum))
        print('rnum: ' + str(rnum))
        lnum, rnum = rnum, len(list(divisors_number(n+1)))

    return n


# start = time.time()
# index = find_triangular_index(500)
# triangle = (index * (index + 1)) / 2
# elapsed = (time.time() - start)
#
# print("result %s returned in %s seconds." % (triangle, elapsed))

def num_divisors(n):
    if n % 2 == 0:
        n = n/2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n/2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n/p
        divisors = divisors * (count + 1)
        p += 2
    return divisors


print(len(list(prime_div_generator(500))))
print(num_divisors(500))