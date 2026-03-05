"""
Calculus Module - Derivatives, integrals, limits, and calculus operations
"""

import math
from typing import Dict, Any, Callable, List
from ..utils.helpers import round_to_decimal


class CalculusSolver:
    """Solves calculus problems with step-by-step explanations"""

    # ------ Power Rule Derivatives ------

    @staticmethod
    def derivative_power_rule(coefficient: float, exponent: float) -> Dict[str, Any]:
        """
        Calculate derivative of coefficient*x^exponent
        Using power rule: d/dx(ax^n) = n*a*x^(n-1)
        """
        new_coefficient = coefficient * exponent
        new_exponent = exponent - 1
        
        steps = [
            f"Function: f(x) = {coefficient}x^{exponent}",
            f"Using Power Rule: d/dx(ax^n) = n*a*x^(n-1)",
            f"f'(x) = {exponent} × {coefficient} × x^({exponent}-1)",
            f"f'(x) = {new_coefficient}x^{new_exponent}"
        ]
        
        return {
            'derivative': f'{new_coefficient}x^{new_exponent}',
            'coefficient': new_coefficient,
            'exponent': new_exponent,
            'steps': steps,
            'formula': f"f'(x) = {new_coefficient}x^{new_exponent}"
        }

    @staticmethod
    def derivative_sum_of_terms(coefficients: List[float], exponents: List[float]) -> Dict[str, Any]:
        """Calculate derivative of a polynomial"""
        if len(coefficients) != len(exponents):
            raise ValueError("Coefficients and exponents must have same length")
        
        result_terms = []
        steps = ["Taking derivative of each term:"]
        
        for coeff, exp in zip(coefficients, exponents):
            if exp == 0:
                steps.append(f"  d/dx({coeff}) = 0")
            else:
                new_coeff = coeff * exp
                new_exp = exp - 1
                if new_exp == 0:
                    result_terms.append(str(new_coeff))
                    steps.append(f"  d/dx({coeff}x^{exp}) = {new_coeff}")
                elif new_exp == 1:
                    result_terms.append(f"{new_coeff}x")
                    steps.append(f"  d/dx({coeff}x^{exp}) = {new_coeff}x")
                else:
                    result_terms.append(f"{new_coeff}x^{new_exp}")
                    steps.append(f"  d/dx({coeff}x^{exp}) = {new_coeff}x^{new_exp}")
        
        result = " + ".join(result_terms).replace("+ -", "- ")
        
        return {
            'derivative': result,
            'steps': steps,
            'formula': f"f'(x) = {result}"
        }

    @staticmethod
    def second_derivative_power_rule(coefficient: float, exponent: float) -> Dict[str, Any]:
        """Calculate second derivative of coefficient*x^exponent"""
        first_deriv_coeff = coefficient * exponent
        first_deriv_exp = exponent - 1
        
        second_deriv_coeff = first_deriv_coeff * first_deriv_exp
        second_deriv_exp = first_deriv_exp - 1
        
        steps = [
            f"Function: f(x) = {coefficient}x^{exponent}",
            f"First derivative: f'(x) = {first_deriv_coeff}x^{first_deriv_exp}",
            f"Second derivative: f''(x) = {second_deriv_coeff}x^{second_deriv_exp}"
        ]
        
        return {
            'second_derivative': f'{second_deriv_coeff}x^{second_deriv_exp}',
            'steps': steps,
            'formula': f"f''(x) = {second_deriv_coeff}x^{second_deriv_exp}"
        }

    # ------ Integration (Anti-derivatives) ------

    @staticmethod
    def integral_power_rule(coefficient: float, exponent: float) -> Dict[str, Any]:
        """
        Calculate indefinite integral of coefficient*x^exponent
        Using power rule: ∫ax^n dx = (a/(n+1))*x^(n+1) + C
        """
        if exponent == -1:
            steps = [
                f"Function: f(x) = {coefficient}/x",
                f"∫{coefficient}/x dx = {coefficient}ln|x| + C"
            ]
            return {
                'integral': f'{coefficient}ln|x| + C',
                'steps': steps,
                'formula': f'∫{coefficient}x^{exponent} dx = {coefficient}ln|x| + C'
            }
        
        new_exponent = exponent + 1
        new_coefficient = coefficient / new_exponent
        
        steps = [
            f"Function: f(x) = {coefficient}x^{exponent}",
            f"Using Power Rule: ∫ax^n dx = (a/(n+1))x^(n+1) + C",
            f"∫{coefficient}x^{exponent} dx = ({coefficient}/{new_exponent})x^{new_exponent} + C",
            f"∫{coefficient}x^{exponent} dx = {round_to_decimal(new_coefficient, 4)}x^{new_exponent} + C"
        ]
        
        return {
            'integral': f'{round_to_decimal(new_coefficient, 4)}x^{new_exponent} + C',
            'steps': steps,
            'formula': f'∫{coefficient}x^{exponent} dx = {round_to_decimal(new_coefficient, 4)}x^{new_exponent} + C'
        }

    # ------ Limits ------

    @staticmethod
    def limit_polynomial(coefficients: List[float], exponents: List[float], x_value: float) -> Dict[str, Any]:
        """Calculate limit of a polynomial as x approaches a value"""
        # For polynomials, limit is just the function value
        result = sum(c * (x_value ** e) for c, e in zip(coefficients, exponents))
        
        steps = [
            f"Find: lim(x→{x_value}) of polynomial",
            f"For continuous functions (like polynomials), we can substitute directly:",
            f"Result = {round_to_decimal(result, 4)}"
        ]
        
        return {
            'limit': result,
            'steps': steps,
            'formula': f'lim = {round_to_decimal(result, 4)}'
        }

    # ------ Critical Points ------

    @staticmethod
    def critical_points_quadratic(a: float, b: float, c: float) -> Dict[str, Any]:
        """Find critical points of f(x) = ax² + bx + c"""
        # Critical point where f'(x) = 0
        # f'(x) = 2ax + b = 0
        # x = -b/2a
        
        x_critical = -b / (2*a)
        y_critical = a*x_critical**2 + b*x_critical + c
        
        # Determine if max or min
        if a > 0:
            extremum = "minimum"
        else:
            extremum = "maximum"
        
        steps = [
            f"Function: f(x) = {a}x² + {b}x + {c}",
            f"Critical point where f'(x) = 0",
            f"f'(x) = {2*a}x + {b}",
            f"Setting f'(x) = 0: {2*a}x + {b} = 0",
            f"x = -b/2a = -{b}/{2*a} = {round_to_decimal(x_critical, 4)}",
            f"y = f({round_to_decimal(x_critical, 4)}) = {round_to_decimal(y_critical, 4)}",
            f"Critical point: ({round_to_decimal(x_critical, 4)}, {round_to_decimal(y_critical, 4)}) - {extremum}"
        ]
        
        return {
            'critical_point': (x_critical, y_critical),
            'type': extremum,
            'steps': steps,
            'formula': f'Critical point: ({round_to_decimal(x_critical, 4)}, {round_to_decimal(y_critical, 4)})'
        }

    # ------ Area Under Curve ------

    @staticmethod
    def definite_integral_polynomial(coefficients: List[float], exponents: List[float], 
                                    a: float, b: float) -> Dict[str, Any]:
        """
        Calculate area under polynomial from x=a to x=b
        Using antiderivative method
        """
        # Calculate antiderivative at boundaries
        def evaluate_antiderivative(x):
            result = 0
            for coeff, exp in zip(coefficients, exponents):
                if exp != -1:
                    result += (coeff / (exp + 1)) * (x ** (exp + 1))
            return result
        
        upper = evaluate_antiderivative(b)
        lower = evaluate_antiderivative(a)
        area = upper - lower
        
        steps = [
            f"Definite integral from x={a} to x={b}",
            f"Find antiderivative and evaluate at bounds",
            f"Area = F({b}) - F({a})",
            f"Area = {round_to_decimal(upper, 4)} - {round_to_decimal(lower, 4)}",
            f"Area = {round_to_decimal(area, 4)}"
        ]
        
        return {
            'area': area,
            'steps': steps,
            'formula': f'Area = {round_to_decimal(area, 4)}'
        }

    # ------ Numerical Differentiation ------

    @staticmethod
    def numerical_derivative(func: Callable, x: float, h: float = 0.0001) -> Dict[str, Any]:
        """
        Calculate derivative numerically using central difference method
        f'(x) ≈ [f(x+h) - f(x-h)] / 2h
        """
        f_plus = func(x + h)
        f_minus = func(x - h)
        derivative = (f_plus - f_minus) / (2 * h)
        
        steps = [
            f"Using numerical differentiation at x = {x}",
            f"Method: Central Difference Formula",
            f"f'(x) ≈ [f(x+h) - f(x-h)] / 2h",
            f"f'({x}) ≈ [f({x + h}) - f({x - h})] / {2*h}",
            f"f'({x}) ≈ {round_to_decimal(derivative, 4)}"
        ]
        
        return {
            'derivative': derivative,
            'steps': steps,
            'formula': f"f'({x}) ≈ {round_to_decimal(derivative, 4)}"
        }

    # ------ Rate of Change ------

    @staticmethod
    def rate_of_change(f_x2: float, f_x1: float, x2: float, x1: float) -> Dict[str, Any]:
        """Calculate average rate of change"""
        rate = (f_x2 - f_x1) / (x2 - x1)
        
        steps = [
            f"Average rate of change from x={x1} to x={x2}",
            f"Formula: [f(x₂) - f(x₁)] / [x₂ - x₁]",
            f"Rate = [{f_x2} - {f_x1}] / [{x2} - {x1}]",
            f"Rate = {f_x2 - f_x1} / {x2 - x1}",
            f"Rate = {round_to_decimal(rate, 4)}"
        ]
        
        return {
            'rate': rate,
            'steps': steps,
            'formula': f'Rate = {round_to_decimal(rate, 4)}'
        }


# Public functions
def derivative_power(coefficient, exponent):
    """Calculate derivative using power rule"""
    return CalculusSolver.derivative_power_rule(coefficient, exponent)['derivative']


def integral_power(coefficient, exponent):
    """Calculate integral using power rule"""
    return CalculusSolver.integral_power_rule(coefficient, exponent)['integral']
