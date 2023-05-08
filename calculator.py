"""
calculator.py - a simple calculator module

This module provides basic arithmetic functions such as addition, subtraction, multiplication and modulus.

Functions:
- add(a: int, b: int) -> int: Returns the sum of two integers.
- subtract(a: int, b: int) -> int: Returns the difference of two integers.
- product(a: int, b: int) -> int: Returns the product of two integers.
- modulo(a: int, b: int) -> int: Returns the modulus of two integers.

Usage:
>>> from calculator import add, subtract, product, modulo
>>> add(2, 3)
5
>>> subtract(5, 2)
3
>>> product(4, 5)
20
>>> modulo(7, 3)
1
"""

def add(a: int, b: int) -> int:
    """Add two numbers.

    Args:
        a (int): First number.
        b (int): Second number.

    Returns:
        int: Sum of a and b.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts integer 'a' from integer 'b'.

    Args:
        a (int): The integer to subtract from 'b'.
        b (int): The integer to be subtracted from.

    Returns:
        int: The result of subtracting 'a' from 'b'.
    """
    return b - a

def modulo(a: int, b: int) -> int:
    """Finds the remainder when integer 'a' is divided by integer 'b'.

    Args:
        a (int): The integer to be divided.
        b (int): The integer to divide 'a' by.

    Returns:
        int: The remainder when 'a' is divided by 'b'.
    """
    return a % b

def product(a: int, b: int) -> int:
    """Multiplies two integers 'a' and 'b'.

    Args:
        a (int): The first integer to be multiplied.
        b (int): The second integer to be multiplied.

    Returns:
        int: The result of multiplying 'a' and 'b'.
    """
    return a * b




