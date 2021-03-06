# %%
import pylab
import os
os.system('cls' if os.name == 'nt' else 'clear')

# at the top and bottom of the file, you see "# %%".
# this is understood by vs code and allows me to
# show the plot in a side-window similar to spyder.


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
        current *= rate

        population.append(current)
        time.append(current_time)

    # instead of returning current, I return the time and population arrays
    return time, population


time, population = exponential_growth(1000, 1.62, 15)
pylab.plot(time, population)
# %%
