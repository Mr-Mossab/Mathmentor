"""
Algebra Module - Equations, polynomials, matrices, and algebraic expressions
"""

import re
import math
from typing import Union, List, Tuple, Dict, Any
from ..utils.helpers import round_to_decimal


class AlgebraSolver:
    """Solves algebraic equations and problems with step-by-step explanations"""

    @staticmethod
    def solve_linear_equation(a: float, b: float, c: float) -> Dict[str, Any]:
        """
        Solve linear equation: ax + b = c
        Returns: x
        """
        if a == 0:
            if b == c:
                return {
                    'result': 'Infinite solutions',
                    'steps': [
                        "Equation: 0x + {} = {}".format(b, c),
                        f"{b} = {c} is always true",
                        "The equation has infinite solutions"
                    ]
                }
            else:
                return {
                    'result': 'No solution',
                    'steps': [
                        "Equation: 0x + {} = {}".format(b, c),
                        f"{b} ≠ {c}",
                        "The equation has no solution"
                    ]
                }
        
        x = (c - b) / a
        steps = [
            f"Equation: {a}x + {b} = {c}",
            f"Subtract {b} from both sides: {a}x = {c - b}",
            f"Divide both sides by {a}: x = {c - b} / {a}",
            f"Solution: x = {round_to_decimal(x, 4)}"
        ]
        
        return {
            'result': x,
            'steps': steps,
            'formula': f'x = {round_to_decimal(x, 4)}'
        }

    @staticmethod
    def solve_quadratic_equation(a: float, b: float, c: float) -> Dict[str, Any]:
        """
        Solve quadratic equation: ax² + bx + c = 0
        Using quadratic formula: x = (-b ± √(b²-4ac)) / 2a
        """
        if a == 0:
            return AlgebraSolver.solve_linear_equation(b, c, 0)
        
        discriminant = b**2 - 4*a*c
        
        steps = [
            f"Equation: {a}x² + {b}x + {c} = 0",
            f"Using quadratic formula: x = (-b ± √(b²-4ac)) / 2a",
            f"a = {a}, b = {b}, c = {c}",
            f"Discriminant (Δ) = b² - 4ac = {b}² - 4({a})({c}) = {discriminant}"
        ]
        
        if discriminant < 0:
            steps.append("Δ < 0, so there are no real solutions (complex solutions exist)")
            return {
                'result': 'No real solutions',
                'steps': steps,
                'discriminant': discriminant
            }
        elif discriminant == 0:
            x = -b / (2*a)
            steps.extend([
                f"√Δ = √{discriminant} = 0",
                f"x = -b / 2a = {-b} / {2*a} = {x}",
                "There is one solution (repeated root)"
            ])
            return {
                'result': x,
                'steps': steps,
                'formula': f'x = {round_to_decimal(x, 4)}'
            }
        else:
            sqrt_discriminant = math.sqrt(discriminant)
            x1 = (-b + sqrt_discriminant) / (2*a)
            x2 = (-b - sqrt_discriminant) / (2*a)
            
            steps.extend([
                f"√Δ = √{discriminant} = {round_to_decimal(sqrt_discriminant, 4)}",
                f"x₁ = (-b + √Δ) / 2a = ({-b} + {round_to_decimal(sqrt_discriminant, 4)}) / {2*a} = {round_to_decimal(x1, 4)}",
                f"x₂ = (-b - √Δ) / 2a = ({-b} - {round_to_decimal(sqrt_discriminant, 4)}) / {2*a} = {round_to_decimal(x2, 4)}",
                "There are two solutions"
            ])
            
            return {
                'result': [x1, x2],
                'steps': steps,
                'formula': f'x₁ = {round_to_decimal(x1, 4)}, x₂ = {round_to_decimal(x2, 4)}'
            }

    @staticmethod
    def solve_system_2x2(a1: float, b1: float, c1: float,
                         a2: float, b2: float, c2: float) -> Dict[str, Any]:
        """
        Solve system of 2 equations with 2 unknowns using elimination method
        a1*x + b1*y = c1
        a2*x + b2*y = c2
        """
        steps = [
            f"System of equations:",
            f"  {a1}x + {b1}y = {c1}",
            f"  {a2}x + {b2}y = {c2}"
        ]
        
        # Calculate determinant
        det = a1*b2 - a2*b1
        
        if det == 0:
            steps.append("Determinant = 0: The system has no unique solution")
            return {
                'result': 'No unique solution',
                'steps': steps
            }
        
        x = (c1*b2 - c2*b1) / det
        y = (a1*c2 - a2*c1) / det
        
        steps.extend([
            f"Using Cramer's rule:",
            f"Determinant = {a1}*{b2} - {a2}*{b1} = {det}",
            f"x = ({c1}*{b2} - {c2}*{b1}) / {det} = {round_to_decimal(x, 4)}",
            f"y = ({a1}*{c2} - {a2}*{c1}) / {det} = {round_to_decimal(y, 4)}"
        ])
        
        return {
            'result': {'x': x, 'y': y},
            'steps': steps,
            'formula': f'x = {round_to_decimal(x, 4)}, y = {round_to_decimal(y, 4)}'
        }

    @staticmethod
    def factor_quadratic(a: float, b: float, c: float) -> Dict[str, Any]:
        """Factor quadratic expression ax² + bx + c"""
        steps = [
            f"Factoring: {a}x² + {b}x + {c}",
            f"Find two numbers that multiply to {a*c} and add to {b}"
        ]
        
        # Find two factors
        ac = a * c
        factors_found = False
        
        for i in range(1, int(abs(ac)) + 1):
            if ac % i == 0:
                j = ac // i
                if i + j == b:
                    steps.append(f"Factors found: {i} and {j}")
                    factors_found = True
                    break
        
        if factors_found:
            steps.append(f"Expression factors as: ({a}x + {i})({x} + {j}/{a})")
            return {
                'result': 'Factored form found',
                'steps': steps
            }
        else:
            steps.append("This quadratic cannot be factored using integers")
            return {
                'result': 'Cannot factor',
                'steps': steps
            }

    @staticmethod
    def expand_binomial(a: float, b: float, power: int) -> Dict[str, Any]:
        """Expand (ax + b)^n using binomial theorem"""
        if power == 2:
            # (ax + b)² = a²x² + 2abx + b²
            coeff_x2 = a**2
            coeff_x1 = 2*a*b
            coeff_x0 = b**2
            
            steps = [
                f"Expand: ({a}x + {b})²",
                f"Formula: (p + q)² = p² + 2pq + q²",
                f"= ({a}x)² + 2({a}x)({b}) + {b}²",
                f"= {coeff_x2}x² + {coeff_x1}x + {coeff_x0}"
            ]
            
            return {
                'result': f'{coeff_x2}x² + {coeff_x1}x + {coeff_x0}',
                'steps': steps,
                'coefficients': {'x²': coeff_x2, 'x': coeff_x1, 'constant': coeff_x0}
            }
        
        elif power == 3:
            # (ax + b)³ = a³x³ + 3a²bx² + 3ab²x + b³
            coeff_x3 = a**3
            coeff_x2 = 3*a**2*b
            coeff_x1 = 3*a*b**2
            coeff_x0 = b**3
            
            steps = [
                f"Expand: ({a}x + {b})³",
                f"Formula: (p + q)³ = p³ + 3p²q + 3pq² + q³",
                f"= {coeff_x3}x³ + {coeff_x2}x² + {coeff_x1}x + {coeff_x0}"
            ]
            
            return {
                'result': f'{coeff_x3}x³ + {coeff_x2}x² + {coeff_x1}x + {coeff_x0}',
                'steps': steps
            }

    @staticmethod
    def simplify_fraction(numerator: int, denominator: int) -> Dict[str, Any]:
        """Simplify a fraction"""
        from ..utils.helpers import gcd
        
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        common_divisor = gcd(numerator, denominator)
        simplified_num = numerator // common_divisor
        simplified_den = denominator // common_divisor
        
        steps = [
            f"Simplify: {numerator}/{denominator}",
            f"GCD({numerator}, {denominator}) = {common_divisor}",
            f"{numerator}/{denominator} = {simplified_num}/{simplified_den}"
        ]
        
        return {
            'result': f'{simplified_num}/{simplified_den}',
            'steps': steps,
            'decimal': simplified_num / simplified_den
        }

    @staticmethod
    def add_fractions(num1: int, den1: int, num2: int, den2: int) -> Dict[str, Any]:
        """Add two fractions"""
        from ..utils.helpers import lcm
        
        # Find LCM of denominators
        common_den = lcm(den1, den2)
        
        # Convert to common denominator
        new_num1 = num1 * (common_den // den1)
        new_num2 = num2 * (common_den // den2)
        
        # Add numerators
        result_num = new_num1 + new_num2
        
        steps = [
            f"Add: {num1}/{den1} + {num2}/{den2}",
            f"LCM({den1}, {den2}) = {common_den}",
            f"= {new_num1}/{common_den} + {new_num2}/{common_den}",
            f"= {result_num}/{common_den}"
        ]
        
        return {
            'result': f'{result_num}/{common_den}',
            'steps': steps,
            'decimal': result_num / common_den
        }

    @staticmethod
    def polynomial_evaluation(coefficients: List[float], x: float) -> Dict[str, Any]:
        """
        Evaluate polynomial at given x value
        coefficients: [a0, a1, a2, ...] for a0 + a1*x + a2*x² + ...
        """
        result = 0
        terms = []
        
        for i, coeff in enumerate(coefficients):
            if i == 0:
                term_value = coeff
                if coeff != 0:
                    terms.append(str(coeff))
            else:
                term_value = coeff * (x ** i)
                if coeff != 0:
                    if i == 1:
                        terms.append(f"{coeff}*x")
                    else:
                        terms.append(f"{coeff}*x^{i}")
            result += term_value
        
        polynomial_str = " + ".join(terms).replace("+ -", "- ")
        
        steps = [
            f"Evaluate: P(x) = {polynomial_str}",
            f"At x = {x}",
            f"P({x}) = {round_to_decimal(result, 4)}"
        ]
        
        return {
            'result': result,
            'steps': steps,
            'formula': f'P({x}) = {round_to_decimal(result, 4)}'
        }


# Public functions for easier access
def solve_linear(a, b, c):
    """Solve linear equation ax + b = c"""
    return AlgebraSolver.solve_linear_equation(a, b, c)


def solve_quadratic(a, b, c):
    """Solve quadratic equation ax² + bx + c = 0"""
    return AlgebraSolver.solve_quadratic_equation(a, b, c)

