"""
Arithmetic Module - Basic mathematical operations
Contains: Addition, Subtraction, Multiplication, Division, Powers, Roots, etc.
"""

import math
from typing import Union, List, Tuple, Dict, Any
from ..utils.helpers import format_step, round_to_decimal, is_perfect_square


class ArithmeticSolver:
    """Solves basic arithmetic problems with step-by-step explanations"""

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Dict[str, Any]:
        """Add two numbers with explanation"""
        result = a + b
        steps = [
            f"Problem: {a} + {b}",
            f"Solution: {a} + {b} = {result}"
        ]
        return {
            'result': result,
            'steps': steps,
            'formula': f'{a} + {b} = {result}'
        }

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Dict[str, Any]:
        """Subtract two numbers with explanation"""
        result = a - b
        steps = [
            f"Problem: {a} - {b}",
            f"Solution: {a} - {b} = {result}"
        ]
        return {
            'result': result,
            'steps': steps,
            'formula': f'{a} - {b} = {result}'
        }

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Dict[str, Any]:
        """Multiply two numbers with explanation"""
        result = a * b
        steps = [
            f"Problem: {a} × {b}",
            f"Solution: {a} × {b} = {result}"
        ]
        return {
            'result': result,
            'steps': steps,
            'formula': f'{a} × {b} = {result}'
        }

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> Dict[str, Any]:
        """Divide two numbers with explanation"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        steps = [
            f"Problem: {a} ÷ {b}",
            f"Solution: {a} ÷ {b} = {result:.4f}"
        ]
        return {
            'result': result,
            'steps': steps,
            'formula': f'{a} ÷ {b} = {result:.4f}'
        }

    @staticmethod
    def power(base: Union[int, float], exponent: int) -> Dict[str, Any]:
        """Calculate power with explanation"""
        result = base ** exponent
        steps = [
            f"Problem: {base}^{exponent}",
            f"This means: {base} × {base}" + (f" × {base}" * (exponent - 2) if exponent > 2 else ""),
            f"Solution: {base}^{exponent} = {result}"
        ]
        return {
            'result': result,
            'steps': steps,
            'formula': f'{base}^{exponent} = {result}'
        }

    @staticmethod
    def square_root(n: Union[int, float]) -> Dict[str, Any]:
        """Calculate square root with explanation"""
        if n < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(n)
        
        if is_perfect_square(n):
            steps = [
                f"Problem: √{int(n)}",
                f"Find a number that when squared equals {int(n)}",
                f"Solution: √{int(n)} = {int(result)}"
            ]
        else:
            steps = [
                f"Problem: √{n}",
                f"Approximating square root",
                f"Solution: √{n} ≈ {round_to_decimal(result, 4)}"
            ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'√{n} = {round_to_decimal(result, 4)}'
        }

    @staticmethod
    def cube_root(n: Union[int, float]) -> Dict[str, Any]:
        """Calculate cube root with explanation"""
        if n >= 0:
            result = n ** (1/3)
        else:
            result = -((-n) ** (1/3))
        
        steps = [
            f"Problem: ³√{n}",
            f"Find a number that when cubed equals {n}",
            f"Solution: ³√{n} = {round_to_decimal(result, 4)}"
        ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'³√{n} = {round_to_decimal(result, 4)}'
        }

    @staticmethod
    def modulo(a: int, b: int) -> Dict[str, Any]:
        """Calculate remainder (modulo) with explanation"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        
        quotient = a // b
        result = a % b
        
        steps = [
            f"Problem: {a} mod {b}",
            f"Divide {a} by {b}: {quotient} remainder {result}",
            f"Solution: {a} mod {b} = {result}"
        ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'{a} mod {b} = {result}'
        }

    @staticmethod
    def percentage(value: float, percent: float) -> Dict[str, Any]:
        """Calculate percentage with explanation"""
        result = (value * percent) / 100
        steps = [
            f"Problem: {percent}% of {value}",
            f"Formula: (value × percent) / 100",
            f"Calculation: ({value} × {percent}) / 100 = {result}"
        ]
        return {
            'result': result,
            'steps': steps,
            'formula': f'{percent}% of {value} = {result}'
        }

    @staticmethod
    def percentage_increase(original: float, increase: float) -> Dict[str, Any]:
        """Calculate percentage increase"""
        result = original + (original * increase / 100)
        difference = result - original
        
        steps = [
            f"Original value: {original}",
            f"Increase: {increase}%",
            f"Increase amount: {original} × {increase}% = {difference}",
            f"New value: {original} + {difference} = {result}"
        ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'New value = {result}'
        }

    @staticmethod
    def percentage_decrease(original: float, decrease: float) -> Dict[str, Any]:
        """Calculate percentage decrease"""
        result = original - (original * decrease / 100)
        difference = original - result
        
        steps = [
            f"Original value: {original}",
            f"Decrease: {decrease}%",
            f"Decrease amount: {original} × {decrease}% = {difference}",
            f"New value: {original} - {difference} = {result}"
        ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'New value = {result}'
        }

    @staticmethod
    def average(numbers: List[Union[int, float]]) -> Dict[str, Any]:
        """Calculate average with explanation"""
        if len(numbers) == 0:
            raise ValueError("Cannot calculate average of empty list!")
        
        total = sum(numbers)
        result = total / len(numbers)
        
        steps = [
            f"Numbers: {numbers}",
            f"Sum: {' + '.join(str(n) for n in numbers)} = {total}",
            f"Count: {len(numbers)}",
            f"Average: {total} ÷ {len(numbers)} = {result}"
        ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'Average = {result}'
        }

    @staticmethod
    def absolute_value(n: Union[int, float]) -> Dict[str, Any]:
        """Calculate absolute value"""
        result = abs(n)
        steps = [
            f"Problem: |{n}|",
            f"Absolute value removes the negative sign",
            f"Solution: |{n}| = {result}"
        ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'|{n}| = {result}'
        }

    @staticmethod
    def distance_between_points(x1: float, y1: float, x2: float, y2: float) -> Dict[str, Any]:
        """Calculate distance between two points"""
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        
        steps = [
            f"Points: ({x1}, {y1}) and ({x2}, {y2})",
            f"Formula: d = √[(x₂-x₁)² + (y₂-y₁)²]",
            f"Calculation: d = √[({x2}-{x1})² + ({y2}-{y1})²]",
            f"d = √[{(x2-x1)**2} + {(y2-y1)**2}]",
            f"d = √{(x2-x1)**2 + (y2-y1)**2}",
            f"Distance = {round_to_decimal(distance, 4)}"
        ]
        
        return {
            'result': distance,
            'steps': steps,
            'formula': f'Distance = {round_to_decimal(distance, 4)}'
        }

    @staticmethod
    def lcm_calc(a: int, b: int) -> Dict[str, Any]:
        """Calculate Least Common Multiple"""
        from ..utils.helpers import lcm
        result = lcm(a, b)
        
        steps = [
            f"Find LCM of {a} and {b}",
            f"The smallest number divisible by both {a} and {b}",
            f"LCM({a}, {b}) = {result}"
        ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'LCM({a}, {b}) = {result}'
        }

    @staticmethod
    def gcd_calc(a: int, b: int) -> Dict[str, Any]:
        """Calculate Greatest Common Divisor"""
        from ..utils.helpers import gcd
        result = gcd(a, b)
        
        steps = [
            f"Find GCD of {a} and {b}",
            f"The largest number that divides both {a} and {b}",
            f"GCD({a}, {b}) = {result}"
        ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'GCD({a}, {b}) = {result}'
        }


# Public functions for easier access
def add(a, b):
    """Add two numbers"""
    return ArithmeticSolver.add(a, b)['result']


def subtract(a, b):
    """Subtract two numbers"""
    return ArithmeticSolver.subtract(a, b)['result']


def multiply(a, b):
    """Multiply two numbers"""
    return ArithmeticSolver.multiply(a, b)['result']


def divide(a, b):
    """Divide two numbers"""
    return ArithmeticSolver.divide(a, b)['result']


def power(base, exponent):
    """Calculate power"""
    return ArithmeticSolver.power(base, exponent)['result']


def sqrt(n):
    """Calculate square root"""
    return ArithmeticSolver.square_root(n)['result']


def cbrt(n):
    """Calculate cube root"""
    return ArithmeticSolver.cube_root(n)['result']
