# Math Imports.
from math import lcm


def mcm(numbers):
    """Fuction To Calculate Least Common Multiple

    Args:
        numbers (List): List of Integers

    Returns:
        int: Least Common Multiple
    """
    try:
        for number in numbers:
            if type(number) != int:
                return{'Error': 'Only Integers'}

        return lcm(*numbers)

    except:
        return{'Error': 'You must send at least two numbers'}


def sum(number):
    """Fuction To Add One To The Number

    Args:
        number (int): Random Number

    Returns:
        int: Result
    """
    try:
        number += 1
        return number
    except:
        return{'Error': 'You must send a integer'}
