"""
Debug demo for COMPSCI235 Lab 1. 
This code will NOT produce the correct result.
Try add a breakpoint and debug the code.

Author: Luke Change (xcha011@aucklanduni.ac.nz) 
Date: 13/07/2022
"""

import numpy as np

MESSAGE = """Enter an integer. This app returns the factorial for this integer (n!)
Press "E" to exit. Value:
"""


def get_factorial(value: int):
    list_values = np.arange(1, value+1)
    factorial = list_values.prod()
    return factorial


def read_input():
    my_input = input(MESSAGE)
    if my_input.lower() == 'e':
        exit()
    if my_input.isnumeric():
        # print(my_input) #testing
        res = get_factorial(int(my_input))
        print(f'{my_input}! = {res}')
    else:
        print(f'{my_input} is not a valid integer!')
    read_input()


if __name__ == '__main__':
    read_input()
