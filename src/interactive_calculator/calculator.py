import logging

logger = logging.getLogger(__name__)


def add(a: float, b: float) -> float:
    """
    Return the sum of a and b.
    """
    result = a + b
    logger.debug(f"Adding {a} + {b} = {result}")
    return result


def subtract(a: float, b: float) -> float:
    """
    Return the difference of a and b.
    """
    result = a - b
    logger.debug(f"Subtracting {a} - {b} = {result}")
    return result


def multiply(a: float, b: float) -> float:
    """
    Return the product of a and b.
    """
    result = a * b
    logger.debug(f"Multiplying {a} * {b} = {result}")
    return result


def divide(a: float, b: float) -> float:
    """
    Return the quotient of a and b.
    Raises ZeroDivisionError if b is zero.
    """
    if b == 0:
        logger.error("Attempt to divide by zero")
        raise ZeroDivisionError("Cannot divide by zero.")
    result = a / b
    logger.debug(f"Dividing {a} / {b} = {result}")
    return result


def power(a: float, b: float) -> float:
    """
    Return a raised to the power of b.
    """
    result = a ** b
    logger.debug(f"Power {a} ** {b} = {result}")
    return result
