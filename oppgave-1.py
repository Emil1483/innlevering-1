from test_utils import test_function, test_function_with_prompt
from input_utils import get_float

from math import log10
import os
os.system('cls' if os.name == 'nt' else 'clear')


# The definition of pH from chemistry is the following:
#     pH = -log(oxonium)
#     where oxonium is the consentration H3O+ in mol/L


def get_pH(oxonium):
    return -log10(oxonium)


test_function(get_pH, [
    10**(-5),
    2,
    4 * 10**(-10)
])

print()  # new line
test_function_with_prompt(get_pH, 'oxonium consentration: ')
