# This **IS** against Presearch TOS and will not be used by me. Please only look at the code and do not try this on Presearch as this **WILL** get you banned.
# This is not sponsored/supported in any means by PreSearch.
# Use with caution, I am not liable for any thing you do with this code.
# This code was made with the intention of showing my knowledge of pyautogui and other Python libraries/features.

# Import libraries
import pyautogui as pygui
import time

# Pyautogui Failsafe (No rouge apps today!)
pygui.FAILSAFE = True

# Make list of words
words = [
    'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine',
    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
    'Seventeen', 'Eightteen', 'Nineteen', 'Twenty', 'Twentyone', 'Twentytwo',
    'Twentythree', 'Twentyfour', 'Twentyfive', 'Twentysix', 'Twentyseven',
    'Twentyeight', 'Twentynine', 'Thirty'
]

# Print information/reminders
print()
print('Starting!')
print('Make sure cursor is in correct area!')

# Give user time to read message and move cursor
time.sleep(10)

# For loop to get words, send words, and repeat.
for word in words:
    print(f'Sending: {word}')
    pygui.click()
    pygui.hotkey('ctrl', 'a')
    pygui.press('backspace')
    pygui.typewrite(word)
    pygui.press('enter')
    time.sleep(5)

# Print notification lettingh user know process is done
print()
print('Done! Hope you like your free crypto!')
