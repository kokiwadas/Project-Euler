# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from functools import reduce


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(numbers):
    return reduce(lambda x, y: (x * y)//gcd(x, y), numbers)


numbers_list = range(1, 21)

print(lcm(numbers_list))
# lcm = numbers[0]
# for i in numbers[1:]:
#     lcm = lcm * i // gr_com_div(lcm, i)
# print(lcm)
