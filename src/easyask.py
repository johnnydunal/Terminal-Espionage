'''
EasyAsk module for Terminal Espionage.
Made to facilitate asking user questions and receiving user feedback.
'''

import src.fancytype as fancytype

def yes_or_no(question):
    while True:
        answer = fancytype.slow_type_and_wait(f"{question} (yes/no): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer == "yes"
        fancytype.slow_type("Please enter 'yes' or 'no'.")