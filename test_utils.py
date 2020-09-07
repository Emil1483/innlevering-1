from input_utils import get_float


def test_function(function, test_parameters):
    check_arguments_count(function)

    print('testing', function.__name__ + ':')

    for test_parameter in test_parameters:
        # indent by 4 spaces
        print(' ' * 4 + format_function_test(function, test_parameter))


def test_function_with_prompt(function, prompt):
    check_arguments_count(function)

    print('testing', function.__name__ + ':')

    # show the prompt indented by 4 spaces
    input_variable = get_float(' ' * 4 + prompt)
    print(' ' * 4 + format_function_test(function, input_variable))


def format_function_test(function, test_parameter):
    return '{0}({1}) = {2}'.format(
        function.__name__, test_parameter, function(test_parameter)
    )


def check_arguments_count(function):
    # I don't want to deal with functions that take multiple parameters
    if function.__code__.co_argcount > 1:
        raise Exception('function must only get one argument')
