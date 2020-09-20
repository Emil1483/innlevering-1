from input_utils import select_from_list, get_float
import os


# I am not going to go into detail about how the Equation
# object works, but I will tell you what it does:

# An Equation is initialized with a list of tuples that
# explain how to get each variable of some equation
# (for example, v = v0 + a * t).
# It then has a get_missing_variable(variables) function
# that returns the value of the missing variable given some
# known variables. If the known variables cannot give
# any missing variable, it returns None.
class Equation:
    def __init__(self, variable_getters):
        self.variable_getters = variable_getters

    def index_of_variable_getter(self, variable_getters, variable_name):
        for i in range(len(variable_getters)):
            variable_getter_name = variable_getters[i][0]
            if variable_getter_name == variable_name:
                return i
        return -1

    def get_variable_from_name(self, variables, name):
        for variable in variables:
            if variable[0] == name:
                return variable[1]

    def get_missing_variable(self, variables):
        missing_variables_getters = self.variable_getters.copy()
        for variable in variables:
            index = self.index_of_variable_getter(
                missing_variables_getters,
                variable[0]
            )
            if index != -1:
                del missing_variables_getters[index]

        if len(missing_variables_getters) != 1:
            return None

        missing_variables_getter = missing_variables_getters[0]

        input_variable_names = [
            getter[0]
            for getter in self.variable_getters
            if getter[0] != missing_variables_getter[0]
        ]
        input_variables = []
        for name in input_variable_names:
            input_variables.append(
                self.get_variable_from_name(variables, name)
            )

        return (
            missing_variables_getter[0],
            missing_variables_getter[1](*input_variables)
        )

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    possible_variables = ['v', 'v0', 'a', 't', 's', 'v_avg']
    equations = [
        # v = v0 + a * t
        Equation([
            ('v', lambda v0, a, t: v0 + a * t),
            ('v0', lambda v, a, t: v - a * t),
            ('a', lambda v, v0, t: (v - v0) / t),
            ('t', lambda v, v0, a: (v - v0) / a),
        ]),
        # s = (v0 + v) * t / 2
        Equation([
            ('s', lambda v0, v, t: (v0 + v) * t / 2),
            ('v0', lambda s, v, t: s * 2 / t - v),
            ('v', lambda s, v0, t: s * 2 / t - v0),
            ('t', lambda s, v0, v: s * 2 / (v0 + v)),
        ]),
        # s = v0 * t + a * t**2 / 2
        Equation([
            ('s', lambda v0, t, a: v0 * t + a * t**2 / 2),
            ('v0', lambda s, t, a: (s - a * t**2 / 2) / t),
            ('t', lambda s, v0, a: (-v0 + (v0**2 + 2 * a * s)**0.5) / a),
            ('a', lambda s, v0, t: (s - v0 * t) * 2 / t**2),
        ]),
        # v**2 = v0**2 + 2 * a * s
        Equation([
            ('v', lambda v0, a, s: (v0**2 + 2 * a * s)**0.5),
            ('v0', lambda v, a, s: (v**2 - 2 * a * s)**0.5),
            ('a', lambda v, v0, s: v**2 - v0**2 / (2 * s)),
            ('s', lambda v, v0, a: v**2 - v0**2 / (2 * a)),
        ]),
        # v_avg = (v0 + v) / 2
        Equation([
            ('v_avg', lambda v0, v: (v0 + v) / 2),
            ('v0', lambda v_avg, v: v_avg * 2 - v),
            ('v', lambda v_avg, v0: v_avg * 2 - v0),
        ])
    ]

    known_variables_names = select_from_list(
        'What variables do you know?', possible_variables)

    # do not event attempt doing anything if the user
    # does not know any variables
    if len(known_variables_names) == 0:
        print('You have to know at least one variable')
        return

    # After the user has given what variabes he knows,
    # he will then be asked to input the value of those variables.
    known_variables = []
    for variable_name in known_variables_names:
        variable_value = get_float(variable_name + ' = ')
        known_variables.append((variable_name, variable_value))
    print() # new line

    done = False
    while not done:
        done = True
        for equation in equations:
            missing = equation.get_missing_variable(known_variables)
            # If the we find a missing variable, add it to the list
            # and make sure to go through each equation again
            # in case the new found variable will give access
            # to new variables from the other equations.
            if missing is not None:
                known_variables.append(missing)
                done = False

    # For the equation s = v0 * t + a * t^2 / 2,
    # t will have two possible values if we solve for it.
    # And I only consider one of them which is why this
    # is only a list of some* of the possible known variables.
    print('Here is a list of some* possible known variables:')
    for name, value in known_variables:
        print('✔', name, '=', value)


if __name__ == '__main__':
    main()
