# Terminal Espionage

'''
A text-based, tactical command-line espionage game built natively in Python.
Act as the remote tactical handler ("the guy in the chair"), orchestrating a high-stakes
facility break-in by managing air-gapped networks, bypassing firewalls, clearing system logs,
and directing your field agent through predictable guard patrols.
'''

import fancytype, easyask, onboarding, operations_center

# Greet user
fancytype.slow_type("Welcome to Terminal Espionage!")
fancytype.slow_type("You are the remote tactical handler, 'the guy in the chair'.")
fancytype.slow_type("Your mission is to guide your field agent through a high-stakes facility break-in.")

# Collect basic user info before beginning game
player_name = fancytype.slow_type_and_wait("Enter your code name: ")
new = easyask.yes_or_no("Would you like to initiate the new recruit onboarding process?")
if new:
    onboarding.start_onboarding(player_name) # Take user to intro/onboarding course
else:
    fancytype.slow_type("Onboarding skipped. Proceeding straight to the Operations Center...")
    operations_center.launch(player_name) # Take user straight to command center