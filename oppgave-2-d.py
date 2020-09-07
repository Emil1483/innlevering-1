# %%
import math
import pylab
import os
os.system('cls' if os.name == 'nt' else 'clear')


def realistic_growth(start, rate, duration, limit, dt):
    current = start

    time = [0]
    population = [current]

    current_time = 0
    while current_time <= duration:
        derivedive = start * math.log(rate) * rate**current_time
        current += dt * derivedive * (1 - current / limit)

        population.append(current)
        time.append(current_time)

        current_time += dt

    return time, population


time, population = realistic_growth(1000, 1.62, 15, 75000, 0.001)
pylab.plot(time, population)
print(population[-1])
# %%
