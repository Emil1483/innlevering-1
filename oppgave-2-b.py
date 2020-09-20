from test_utils import test_function

import os
os.system('cls' if os.name == 'nt' else 'clear')


def exponential_growth(start, rate, duration):
    # current refers to the current population in CFU
    current = start

    time = [0]
    population = [current]
    # For each hour, the population should be (1 + rate) of
    # the current population. For example, if the rate is 50 %,
    # the current population should become 1.5 of itself for
    # each hour that passes.
    for current_time in range(1, duration + 1):
        current *= 1 + rate

        population.append(current)
        time.append(current_time)

    return current


test_function(exponential_growth, [
    [1000, .62, 15],
])
