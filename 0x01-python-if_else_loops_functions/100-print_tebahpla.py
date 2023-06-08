#!/usr/bin/python3


i = 0
for char in range(ord('z'), ord('A') - 1, -1):
    print("{}".format(chr(char + i)), end="")
    i = 32 if i == 0 else 0
