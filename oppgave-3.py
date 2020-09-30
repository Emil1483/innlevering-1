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
    # clears the console 🧹
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
            ('t', lambda s, v0, a: ((-v0 + (v0**2 + 2 * a * s)**0.5) / a,
                                    (-v0 - (v0**2 + 2 * a * s)**0.5) / a)),
            ('a', lambda s, v0, t: (s - v0 * t) * 2 / t**2),
        ]),
        # v**2 = v0**2 + 2 * a * s
        Equation([
            ('v', lambda v0, a, s: ((v0**2 + 2 * a * s)**0.5,
                                    (-(v0**2 + 2 * a * s)**0.5))),
            ('v0', lambda v, a, s: ((v**2 - 2 * a * s)**0.5,
                                    (-(v**2 - 2 * a * s)**0.5))),
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
        'What variables do you know? 😳👉👈', possible_variables)

    # do not event attempt doing anything if the user
    # does not know any variables! 🤨🔪
    if len(known_variables_names) == 0:
        print('You have to know at least one variable')
        return

    # After the user has given what variabes he knows,
    # he will then be asked to input the value of those variables.
    known_variables = []
    for variable_name in known_variables_names:
        variable_value = get_float(variable_name + ' = ')
        known_variables.append((variable_name, variable_value))
    print()  # new line

    total_variables = []
    total_variables.append(known_variables)

    # here, we find the variables that corresponds
    # with the given variables from the user input

    # total_variables is a list of variable columns
    # a variable column is a list of variables that
    # corresponds with the known variables (from user input)
    # the reason there are multiple variable columns is because
    # t might be one of two variables. This happens for example
    # when we throw a ball straight up and want to know when it is 5
    # meters above it's initial position. And since this often
    # happens at two different points in time, there should be two
    # variable columns that each contain a different value for t
    done = False
    while not done:
        done = True
        # go through each equation in search of
        # more variables for each variable column
        for equation in equations:
            for variable_column in total_variables:
                missing = equation.get_missing_variable(variable_column)
                if missing is not None:
                    done = False

                    # convert the missing variable into a list
                    # for example, ('t', (1, -1)) becomes
                    # [('t', 1), ('t', -1)] and
                    # ('t', 1) becomes [('t', 1)]
                    name, values = missing
                    is_tuple = type(values) is tuple
                    if not is_tuple:
                        values = (values,)
                    missing = [(name, value) for value in values]

                    # the equation x^2 = 1 has two valid solutions.
                    # as a result, get_missing_variable can return
                    # will possible return two variable values.
                    # if the the function returns only one solution,
                    # we add that to the current 'variable column'.
                    # and for each additional solution, we make
                    # a copy of the current variable column and
                    # appends that result to the copy and append
                    # that copy to 'total variables'
                    for missing_variable in missing[1:]:
                        new_column = variable_column.copy()
                        new_column.append(missing_variable)
                        total_variables.append(new_column)
                    variable_column.append(missing[0])

    # the equation v**2 = v0**2 + 2 * a * s gives
    # two possible solutions for v and v0, one positive
    # and one negative. But the sign of the variable
    # entirely depends on the value of t, but this
    # equation does not depend on t. This causes
    # this equation to only give the correct value
    # half of the time.

    # we will now delete each column that contains bad variables.
    # this happens due to the problem above and
    # when the user inputs variables that does not correspond
    # with each other

    # we loop through the total variables in reverse
    # because we might delete from it while we loop
    for variable_column in reversed(total_variables):
        for variable in variable_column:
            # for each variable in each column, check if that
            # variable is correct by removing it and
            # use an equation to get it back. If the variable
            # is not the same, the entire column is bad and should
            # be deleted.
            copy = variable_column.copy()
            copy.remove(variable)
            variable_bad = True
            for equation in equations:
                missing = equation.get_missing_variable(copy)
                if missing is not None:
                    # due to calculations being imprecise,
                    # we round the values before checking them
                    variable_bad = round(
                        missing[1], 5) != round(variable[1], 5)
                    break
            if variable_bad:
                total_variables.remove(variable_column)
                break

    if len(total_variables) == 0:
        print('The variables you submitted did not correspond with each other')
    else:
        print('Here is a list of all possible known variables:')
        for variable_column in total_variables:
            print()
            for name, value in variable_column:
                print('✔', name, '=', value)


if __name__ == '__main__':
    main()
