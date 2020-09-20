import sys
import os

from input_utils import clear_prev_lines
from loading_utils import build_loading_string

os.system('cls' if os.name == 'nt' else 'clear')

results = []
for x in range(-100, 101):
    value = (x + 100) / 200 # float 0-1
    clear_prev_lines(1)
    print(build_loading_string(value, 20))
    for y in range(-100, 101):
        for z in range(-100, 101):
            number = x**3 + y**3 + z**3
            
            # this checks if the number is between 0 and 10
            if number in range(11):
                results.append((x, y, z, number))
                

for x, y, z, n in results:
    print(f'({x})³ + ({y})³ + ({z})³ = {n}')
print('total integer solutions:', len(results))
