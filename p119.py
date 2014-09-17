#!/usr/bin/env python
"""
https://projecteuler.net/problem=119

The number 512 is interesting because it is equal to the sum of its digits
raised to some power: 5 + 1 + 2 = 8, and pow(8, 3) = 512. Another example of a
number with this property is 614656 = pow(28, 4).

We shall define an to be the nth term of this sequence and insist that a number
must contain at least two digits to have a sum.

You are given that a2 = 512 and a10 = 614656.

Find a30.

"""


def split(x):
    digits = []
    while x > 0:
        digits.append(x % 10)
        x /= 10
    return digits


def a(n):
    results = []

    for base in xrange(2, 100):
        for power in xrange(1, 100):
            x = base ** power
            if x > 9 and sum(split(x)) == base:
                results.append(x)

    results = sorted(results)
    return results[n - 1]


if __name__ == '__main__':
    print a(30)
