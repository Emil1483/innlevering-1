import sys
import os
import keyboard

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def clear_prev_lines(num_lines):
    for _ in range(num_lines):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def select_from_list(prompt, options):
    class State:
        def __init__(self, prompt, options):
            self.cursor = 0
            self.selected = []
            self.prompt = prompt
            self.options = options
            self.show_menu(clear=False)

        def show_menu(self, clear=True):
            if clear:
                clear_prev_lines(len(self.options) + 1)
            print(self.prompt, '(Press SPACE to select and ENTER to continue)')
            for i in range(len(self.options)):
                arrow = '<' if self.cursor == i else ''
                check_box = '✅' if i in self.selected else '🟩'
                print(check_box, self.options[i], arrow)

        def change_cursor(self, value):
            new_value = self.cursor + value
            if new_value < 0 or new_value >= len(self.options):
                return
            self.cursor += value
            self.show_menu()

        def toggle_selected(self):
            if self.cursor in self.selected:
                self.selected.remove(self.cursor)
            else:
                self.selected.append(self.cursor)
            self.show_menu()
        
        def show_end_menu(self):
            self.cursor = -1
            self.show_menu()
            print()

    state = State(prompt, options)

    keyboard.add_hotkey('up', lambda: state.change_cursor(-1))
    keyboard.add_hotkey('down', lambda: state.change_cursor(1))
    keyboard.add_hotkey('space', lambda: state.toggle_selected())
    keyboard.add_hotkey('enter', lambda: state.show_end_menu())

    keyboard.wait('enter')

    keyboard.unhook_all()
    input()
    sys.stdout.write(CURSOR_UP_ONE)

    return [options[selected] for selected in state.selected]


def get_float(prompt):
    error=False
    while True:
        try:
            value=input(prompt)
            if error:
                clear_prev_lines(2)
                print(prompt + value)
            return float(value)
        except ValueError:
            clear_prev_lines(1)
            error=True
            print("\"{0}\"".format(value), "is not a valid input,",
                  "please try again")


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("{0} is an awesome number 😸. Thank you.".format(get_float("float: ")))
