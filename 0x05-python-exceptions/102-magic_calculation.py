#!/usr/bin/python3

import dis

def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += (a ** b) / i
        except Exception as e:
            result = b + a
            break

    return result

bytecode = dis.Bytecode(magic_calculation)
for instruction in bytecode:
    print(instruction)
