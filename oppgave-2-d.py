# %%
import math
import pylab
import os
os.system('cls' if os.name == 'nt' else 'clear')

# at the top and bottom of the file, you see "# %%".
# this is understood by vs code and allows me to
# show the plot in a side-window similar to spyder.


# dt refers to the time step. dt should be as small as
# possible for accuracy
def realistic_growth(start, rate, duration, limit, dt):
    # current refers to the current population in CFU
    current = start

    time = [0]
    population = [current]

    # For each hour, the population should be (1 + rate) of
    # the current population. For example, if the rate is 50 %,
    # the current population should become 1.5 of itself for
    # each hour that passes.

    current_time = dt
    while current_time <= duration:
        # the original function was p(t) = a * r^t
        # where p is the population after t hours,
        # a is the initial population and r is the
        # rate at which the population grows.
        # dp / dt = p'(t) = a * ln(r) * r^t
        # dp = dt * a * ln(r) * r^t
        # dp represents how much the current population
        # should change for each calculation.
        dp = dt * start * math.log(rate) * rate ** current_time

        # if this was a normal exponential function,
        # we could simply write: current += dp. However,
        # this does not consider the limit.
        # I imagine the limit to cause the population change
        # to go drop to 0 as the population approaches the limit.
        # As such, I multiply the change with (1 - current / limit)
        # because this expression drops to 0 as the current approaches
        # the limit.
        current += dp * (1 - current / limit)

        # I think the plot looks very realistic because it
        # clearly slows down towards the end, just like
        # a population with a limiting factor should.
        # this becomes more apparent as you increase
        # the time from 15 hours to 20 hours.

        population.append(current)
        time.append(current_time)

        current_time += dt

    return time, population


# the limit is 750 000 because the population is limited
# to 1 500 CFU per mL and there is 500 mL. 1 500 * 500 = 750 000
time, population = realistic_growth(1000, 1.62, 15, 750000, 0.001)
pylab.plot(time, population)

# population[-1] is the last element in the array
print(population[-1])
# %%
