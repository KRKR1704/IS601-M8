# Author: Roopesh Kumar Reddy Kaipa
# Date: 10/27/2025
"""
Module: operations.py

This module contains basic arithmetic functions that perform addition, subtraction,
multiplication, and division of two numbers. These functions are foundational for
building more complex applications, such as calculators or financial tools.

Functions:
- add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the sum of a and b.
- subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the difference when b is subtracted from a.
- multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]: Returns the product of a and b.
- divide(a: Union[int, float], b: Union[int, float]) -> float: Returns the quotient when a is divided by b. Raises ValueError if b is zero.

Usage:
These functions can be imported and used in other modules or integrated into APIs
to perform arithmetic operations based on user input.
"""

from typing import Union
import logging

Number = Union[int, float]

logger = logging.getLogger(__name__)

def add(a: Number, b: Number) -> Number:
    """
    Add two numbers and return the result.

    Parameters:
    - a (int or float): The first number to add.
    - b (int or float): The second number to add.

    Returns:
    - int or float: The sum of a and b.

    Example:
    >>> add(2, 3)
    5
    >>> add(2.5, 3)
    5.5
    """
    logger.debug("add called with a=%s, b=%s", a, b)
    result = a + b
    logger.info("add result: %s + %s = %s", a, b, result)
    return result

def subtract(a: Number, b: Number) -> Number:
    """
    Subtract the second number from the first and return the result.

    Parameters:
    - a (int or float): The number from which to subtract.
    - b (int or float): The number to subtract.

    Returns:
    - int or float: The difference between a and b.

    Example:
    >>> subtract(5, 3)
    2
    >>> subtract(5.5, 2)
    3.5
    """
    logger.debug("subtract called with a=%s, b=%s", a, b)
    result = a - b
    logger.info("subtract result: %s - %s = %s", a, b, result)
    return result

def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers and return the product.

    Parameters:
    - a (int or float): The first number to multiply.
    - b (int or float): The second number to multiply.

    Returns:
    - int or float: The product of a and b.

    Example:
    >>> multiply(2, 3)
    6
    >>> multiply(2.5, 4)
    10.0
    """
    logger.debug("multiply called with a=%s, b=%s", a, b)
    result = a * b
    logger.info("multiply result: %s * %s = %s", a, b, result)
    return result

def divide(a: Number, b: Number) -> float:
    """
    Divide the first number by the second and return the quotient.

    Parameters:
    - a (int or float): The dividend.
    - b (int or float): The divisor.

    Returns:
    - float: The quotient of a divided by b.

    Raises:
    - ValueError: If b is zero, as division by zero is undefined.

    Example:
    >>> divide(6, 3)
    2.0
    >>> divide(5.5, 2)
    2.75
    >>> divide(5, 0)
    Traceback (most recent call last):
        ...
    ValueError: Cannot divide by zero!
    """
    # Check if the divisor is zero to prevent division by zero
    logger.debug("divide called with a=%s, b=%s", a, b)
    if b == 0:
        logger.error("divide attempted with divisor 0: a=%s, b=%s", a, b)
        # Raise a ValueError with a descriptive message
        raise ValueError("Cannot divide by zero!")

    # Perform division of a by b and return the result as a float
    result = a / b
    logger.info("divide result: %s / %s = %s", a, b, result)
    return result

def power(a: Number, b: Number) -> float:
    """
    Raise a to the power of b and return the result as a float.

    Parameters:
    - a (int or float): The base.
    - b (int or float): The exponent.

    Returns:
    - float: The result of a ** b.

    Raises:
    - ValueError: If the operation is invalid (for example, negative base with
      a fractional exponent which is not supported in real numbers).

    Example:
    >>> power(2, 3)
    8.0
    >>> power(9, 0.5)
    3.0
    """
    import math

    logger.debug("power called with a=%s, b=%s", a, b)
    try:
        result = math.pow(a, b)
    except Exception as exc:
        logger.error("power operation failed for a=%s, b=%s: %s", a, b, exc)
        raise ValueError("Invalid power operation")

    if result != result:
        logger.error("power result is not a real number for a=%s, b=%s", a, b)
        raise ValueError("Result is not a real number")

    logger.info("power result: %s ** %s = %s", a, b, result)
    return result
