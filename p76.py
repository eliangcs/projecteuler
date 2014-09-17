"""
https://projecteuler.net/problem=76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two
positive integers?

"""

p_cache = {}


def p(n, k):
    """
    Return the number of ways of writing n as a sum where the minimum component
    number is k.

    For example, p(5, 1) = 5 because it has the following five ways:

        4 + 1
        3 + 1 + 1
        2 + 2 + 1
        2 + 1 + 1 + 1
        1 + 1 + 1 + 1 + 1

    And p(5, 2) = 1 because it only has one way:

        3 + 2

    """
    # Base case
    if n == 2:
        if k == 1:
            return 1
        return 0

    if n == 3:
        if k == 1:
            return 2
        return 0

    if k > n / 2:
        return 0

    if (n, k) not in p_cache:
        # Induction
        p_cache[(n, k)] = sum([p(n - k, i) for i in xrange(k, n / 2 + 1)]) + 1

    return p_cache[(n, k)]


def get_num_ways(n):
    return sum([p(n, k) for k in xrange(1, n / 2 + 1)])


if __name__ == '__main__':
    print get_num_ways(100)
