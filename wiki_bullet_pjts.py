#! pyhton 3
# Bullet pointer.py - adds bullets to start of lists

import pyperclip
text = pyperclip.paste()

#separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):       # loop through all indexes in the "lines" list
    lines[i] = '* '+ lines[i]     #add star to each string in "lines" list

text = '\n'.join(lines)   # python expects single string not a list of strings
pyperclip.copy(text)

