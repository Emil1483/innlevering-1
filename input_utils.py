import sys
import os
import keyboard

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def clear_prev_lines(num_lines):
    for _ in range(num_lines):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def up(state):
    state.changeCurrent(-1)


def down(state):
    state.changeCurrent(1)


def space(state):
    state.toggleSelected()


def enter(state):
    clear_prev_lines(len(state.options) + 1)


class State:
    def __init__(self, prompt, options):
        self.current = 0
        self.selected = []
        self.prompt = prompt
        self.options = options
        self.show_menu(clear=False)

    def show_menu(self, clear=True):
        if clear:
            clear_prev_lines(len(self.options) + 1)
        print(self.prompt, '(Press SPACE to select and ENTER to continue)')
        for i in range(len(self.options)):
            arrow = '<' if self.current == i else ''
            check_box = '✅' if i in self.selected else '🟩'
            print(check_box, self.options[i], arrow)

    def changeCurrent(self, value):
        new_value = self.current + value
        if new_value < 0 or new_value >= len(self.options):
            return
        self.current += value
        self.show_menu()

    def toggleSelected(self):
        if self.current in self.selected:
            self.selected.remove(self.current)
        else:
            self.selected.append(self.current)
        self.show_menu()


def select_from_list(prompt, options):
    state = State(prompt, options)

    keyboard.add_hotkey('up', lambda: up(state))
    keyboard.add_hotkey('down', lambda: down(state))
    keyboard.add_hotkey('space', lambda: space(state))
    keyboard.add_hotkey('enter', lambda: enter(state))
    keyboard.wait('enter')
    keyboard.unhook_all()
    input() # I have no fucking idea why this fixes the bug that I tried to fix for 4 hours or so ❤
    sys.stdout.write(CURSOR_UP_ONE)

    return state.selected


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
    os.system('cls' if os.name == 'nt' else 'clear')
    print("{0} is an awesome number 😸. Thank you.".format(get_float("float: ")))
