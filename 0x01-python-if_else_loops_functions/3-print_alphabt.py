#!/usr/bin/python3

# Iterate through lowercase letters from 'a' to 'z' excluding 'q' and 'e'
for letter in range(97, 123):
    if chr(letter) not in ['q', 'e']:
        print("{}".format(chr(letter)), end='')

