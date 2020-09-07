def test_function(function, test_parameters):
    print('testing', function.__name__, ':')
    for test_parameter in test_parameters:
        print(
            ' ' * 4,  # indent by 4 spaces
            str(test_parameter) + ':',  # show the input of the function
            function(test_parameter)  # show the output of the function
        )
