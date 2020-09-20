from input_utils import clear_prev_lines

# this function returns the spinning thing


def get_indicator(integer):
    # switches don't exist in python. Instead, make a
    # dictionary and look up the value. This
    # is equivalent to the following:
    '''
    switch(integer) {
        case (0):
            return '/';
        case (1):
            return '-';
        case (2):
            return '\\';
        case (3):
            return '|';
    }
    '''

    switcher = {
        0: '/',
        1: '-',
        # '\' make python expect a key character
        # like '\n'. '\\' causes python to ignore this
        2: '\\',
        3: '|',
    }
    return switcher[round(integer) % 4]


def build_loading_string(value, bar_length=10):
    # value is a double 0-1
    persentage = round(value * 100)
    bars = '█' * round(value * bar_length)
    spaces = ' ' * round((1 - value) * bar_length)
    indicator = get_indicator(persentage)
    return f'{persentage} % |{bars}{spaces}| {indicator}'
