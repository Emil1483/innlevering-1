from input_utils import clear_prev_lines

def getIndicator(integer):
    switcher = {
        0: '/',
        1: '-',
        2: '\\',
        3: '|',
    }
    return switcher[round(integer) % 4]

def build_loading_string(value, bar_length = 10):
    persentage = round(value * 100)
    bars = '█' * round(value * bar_length)
    spaces = ' ' * round((1 - value) * bar_length)
    indicator = getIndicator(persentage)
    return f'{persentage} % |{bars}{spaces}| {indicator}'