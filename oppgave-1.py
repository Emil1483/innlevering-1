from math import log10

from test_utils import test_function

"""
The definition of pH from chemistry is the following:
    pH = -log(oxonium)
    where oxonium is the consentration H3O+ in mol/L
"""


def get_pH(oxonium):
    return -log10(oxonium)


test_function(get_pH, [
    10**(-5),
    2,
    4 * 10**(-10)
])
