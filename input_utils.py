import sys
import os

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def clear_prev_lines(num_lines):
    for _ in range(num_lines):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def get_float(prompt):
    error = False
    while True:
        try:
            value = input(prompt)
            if error:
                clear_prev_lines(2)
                print(prompt + value)
            return float(value)
        except ValueError:
            clear_prev_lines(1)
            error = True
            print("\"{0}\"".format(value), "is not a valid input,",
                  "please try again")


if __name__ == "__main__":
    os.system('cls')
    print("{0} is an awesome number 😸. Thank you.".format(get_float("float: ")))
