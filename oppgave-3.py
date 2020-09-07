from input_utils import select_from_list
import time

known_variables = select_from_list('What variables do you know?', ['v', 'v0', 'a', 't', 's'])

print(known_variables)