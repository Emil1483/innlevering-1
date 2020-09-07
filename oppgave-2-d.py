# %%
import math
import pylab
import os
os.system('cls' if os.name == 'nt' else 'clear')


def exponential_growth(start, rate, duration):
    current = start

    time = [0]
    population = [current]
    for current_time in range(duration):
        current += start * math.log(rate) * rate**current_time

        population.append(current)
        time.append(current_time + 1)

    return time, population


time, population = exponential_growth(1000, 1.62, 15)
pylab.plot(time, population)
# %%
