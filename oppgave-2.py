#%% 
from test_utils import test_function

import pylab
import os
os.system('cls' if os.name == 'nt' else 'clear')


def exponential_growth(start, rate, duration):
    current = start

    time = [0]
    population = [current]
    for current_time in range(1, duration + 1):
        current *= 1 + rate

        population.append(current)
        time.append(current_time)

    return current, time, population

def exponential_growth_simple(start, rate, duration):
    growth = exponential_growth(start, rate, duration)
    return growth[0]


test_function(exponential_growth_simple, [
    [1000, .62, 15],
    [1000, .62, 16],
])

growth = exponential_growth(1000, .62, 15)
pylab.plot(growth[1], growth[2])

# %%
