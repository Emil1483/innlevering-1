from test_utils import test_function

import os
os.system('cls' if os.name == 'nt' else 'clear')


def exponential_growth(start, rate, duration):
    # current refers to the current population in CFU
    current = start

    # For each hour, the population should be (1 + rate) times
    # the current population. For example, if the rate is 50 %,
    # the current population should become 1.5 times itself for
    # each hour that passes.
    for _ in range(1, duration + 1):
        current *= 1 + rate

    return current


test_function(exponential_growth, [
    [1000, .62, 15],
])
