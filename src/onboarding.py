'''
This module controls the onboarding (tutorial) process to teach users how everything works.
'''

import fancytype

# Gives Flint a distinct visual tag in the scrolling terminal
def print_flint(text):
    print("\033[33m" + "[FLINT]:" + "\033[0m", end=" ") # Print the Flint tag in yellow
    fancytype.slow_type(text, 0.03, 1) # Prints actual message
    

def start_onboarding(player_name):
    print_flint("Greetings! My name is Flint, and I'll be your guide for this onboarding process.")





# TESTING ONBOARDING
start_onboarding("Johnny")