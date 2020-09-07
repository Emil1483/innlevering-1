import sys
import os
os.system('cls' if os.name == 'nt' else 'clear')

results = []
for n in range(11):
    print(round(n * 100 / 11, 1), '%', end='\r')
    for x in range(-100, 101):
        for y in range(-100, 101):
            for z in range(-100, 101):
                if x**3 + y**3 + z**3 == n:
                    results.append((x, y, z, n))
for result in results:
    x, y, z, n = result
    print('{0}^3 + {1}^3 + {2}^3 = {3}^3'.format(x, y, z, n))
print('total integer solutions:', len(results))
