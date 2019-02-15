
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


if __name__ == '__main__':
    start = datetime.now()
    print(num_ways(997, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}, {}))
    print(datetime.now() - start)
