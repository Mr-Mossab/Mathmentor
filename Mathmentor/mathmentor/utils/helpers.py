"""
Utility functions for MathMentor library
"""

import math
from typing import Union, List, Tuple, Any
from fractions import Fraction


def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Calculate Greatest Common Divisor"""
    while b:
        a, b = b, a % b
    return abs(a)


def lcm(a: int, b: int) -> int:
    """Calculate Least Common Multiple"""
    return abs(a * b) // gcd(a, b)


def is_perfect_square(n: float) -> bool:
    """Check if a number is a perfect square"""
    if n < 0:
        return False
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n


def factorial(n: int) -> int:
    """Calculate factorial of n"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combination(n: int, r: int) -> int:
    """Calculate C(n, r) - combination"""
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))


def permutation(n: int, r: int) -> int:
    """Calculate P(n, r) - permutation"""
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)


def round_to_decimal(num: float, decimals: int = 2) -> float:
    """Round number to specific decimal places"""
    return round(num, decimals)


def format_step(step: int, description: str, formula: str = "") -> str:
    """Format a step in the solution"""
    if formula:
        return f"Step {step}: {description}\n  Formula: {formula}"
    return f"Step {step}: {description}"
