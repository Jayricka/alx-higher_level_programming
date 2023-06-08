#!/usr/bin/python3


output = ''
for i in range(ord('z'), ord('A') - 1, -1):
    letter = chr(i)
    case = 'lowercase' if i % 2 == 1 else 'uppercase'
    output += f'{letter}{case}'

print(output)
