'''
Fancy type module for Terminal Espionage.
Includes functions for cooler typing styles, such as slow typing and slow typing with user input.
'''

import time

# Types the given text slowly, character by character
def slow_type(text, delay_during=0.04, delay_after=0.5, newline=True):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay_during)
    if newline:
        print()
    time.sleep(delay_after)

# Types the given text slowly, character by character, and waits for user input after
def slow_type_and_wait(text, delay_during=0.04, delay_after=0.5):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay_during)
    answer = input()
    time.sleep(delay_after)
    return answer