from input_utils import get_float
from re import sub


def test_function(function, test_parameters):
    print('testing', function.__name__ + ':')

    for test_parameter in test_parameters:
        # indent by 4 spaces
        print(' ' * 4 + format_function_test(function, test_parameter))


def test_function_with_prompt(function, prompt):
    print('testing', function.__name__ + ':')

    # show the prompt indented by 4 spaces
    input_variable = get_float(' ' * 4 + prompt)
    print(' ' * 4 + format_function_test(function, input_variable))


def format_function_test(function, function_input):
    is_list = type(function_input) is list
    return '{0}({1}) = {2}'.format(
        function.__name__,
        # if the function_input is a list, remove '[' and ']' from the string
        sub(r'[\[\]]', '', str(function_input)),
        # if the function_input is a list, use *function_input to split the arguments
        function(*function_input) if is_list else function(function_input)
    )
