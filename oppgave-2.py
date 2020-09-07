import os
os.system('cls' if os.name == 'nt' else 'clear')

def exponential_growth(start, rate, duration):
    current = start
    for _ in range(duration):
        current *= 1 + rate
        print(current)
    return current

print(exponential_growth(1000, .62, 15))