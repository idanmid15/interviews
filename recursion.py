
from datetime import datetime


def num_ways(num_stairs, allowed_steps, visited_steps):
    """
    Ways to climb N stairs

    There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the
    number of unique ways you can climb the staircase. The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

    Generalize the problem to take as input a set of allowed steps
    For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    """

    if num_stairs < 0:
        return 0
    if num_stairs == 0:
        return 1
    if num_stairs in visited_steps:
        return visited_steps[num_stairs]
    accumulated_ways = 0
    for allowed_step in allowed_steps:
        accumulated_ways += num_ways(num_stairs - allowed_step, allowed_steps, visited_steps)
    visited_steps[num_stairs] = accumulated_ways
    return accumulated_ways


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    """
    cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
    For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
    """
    def get_first(a, _):
        return a
    return pair(get_first)


def cdr(pair):
    def get_last(_, b):
        return b
    return pair(get_last)


def amount_decoded_messages(message):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
    You can assume that the messages are decodable. For example, '001' is not allowed.
    This is the naive solution, memoization can be used here
    """
    if message == '' or len(message) == 1:
        return 1
    if 26 >= int(message[0:2]) >= 10:
        return amount_decoded_messages(message[2:]) + amount_decoded_messages(message[1:])
    return amount_decoded_messages(message[1:])


if __name__ == '__main__':
    start = datetime.now()
    print(num_ways(997, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, {}))
    print(datetime.now() - start)
    print(car(cons(3, 4)))  # 3
    print(cdr(cons(3, 4)))  # 4
    print(cdr(cdr(cons(3, cons(4, 5)))))  # 5
    print(car(cdr(cons(3, cons(4, 5)))))  # 4
    print(amount_decoded_messages('111'))  # 3
