import keyboard

import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')

current = 1
selected = []
options = ['v', 'v0', 'a', 't', 's']

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'


def clear_prev_lines(num_lines):
    for _ in range(num_lines):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def show_menu():
    global current
    clear_prev_lines(len(options) + 1)
    print('what variables do you know? press SPACE to select and ENTER to confirm')
    for i in range(len(options)):
        arrow = '<' if current == i else ''
        check_box = '✅' if i in selected else '🟩'
        print(check_box, options[i], arrow)


def up():
    global current
    if current <= 0:
        return
    current -= 1
    show_menu()


def down():
    global current
    if current >= len(options) - 1:
        return
    current += 1
    show_menu()

def space():
    global current
    if current in selected:
        selected.remove(current)
    else:
        selected.append(current)
    show_menu()

def enter():
    clear_prev_lines(len(options) + 1)
    print([options[select] for select in selected])

show_menu()
keyboard.add_hotkey('up', up)
keyboard.add_hotkey('down', down)
keyboard.add_hotkey('space', space)
keyboard.add_hotkey('enter', enter)

keyboard.wait('enter')

print('hello \n' * 10)