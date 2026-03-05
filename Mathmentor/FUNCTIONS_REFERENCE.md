# MathMentor - Advanced Features Documentation

## Comprehensive Function Reference

### Arithmetic Module (25+ Functions)

#### Basic Operations
- `add(a, b)` - Add two numbers
- `subtract(a, b)` - Subtract two numbers
- `multiply(a, b)` - Multiply two numbers
- `divide(a, b)` - Divide two numbers with error handling

#### Powers & Roots
- `power(base, exponent)` - Calculate base^exponent
- `sqrt(n)` - Square root calculation
- `cbrt(n)` - Cube root calculation

#### Advanced Operations
- `percentage(value, percent)` - Calculate percentage of value
- `percentage_increase(original, increase)` - Calculate increase
- `percentage_decrease(original, decrease)` - Calculate decrease
- `modulo(a, b)` - Calculate remainder (a mod b)
- `average(numbers)` - Calculate average of list
- `absolute_value(n)` - Absolute value
- `distance_between_points(x1, y1, x2, y2)` - Distance formula
- `gcd_calc(a, b)` - Greatest Common Divisor
- `lcm_calc(a, b)` - Least Common Multiple
- `ArithmeticSolver` - Class with all above methods

### Algebra Module (20+ Functions)

#### Equation Solving
- `solve_linear_equation(a, b, c)` - Solve ax + b = c
- `solve_quadratic_equation(a, b, c)` - Solve ax² + bx + c = 0
- `solve_system_2x2()` - Solve 2x2 system using Cramer's rule

#### Polynomial Operations
- `factor_quadratic(a, b, c)` - Factor ax² + bx + c
- `expand_binomial(a, b, power)` - Expand (ax + b)^n
- `polynomial_evaluation(coefficients, x)` - Evaluate polynomial at x

#### Fractions & Simplification
- `simplify_fraction(num, den)` - Simplify fraction
- `add_fractions(num1, den1, num2, den2)` - Add fractions
- `AlgebraSolver` - Class with all methods

### Geometry Module (35+ Functions)

#### 2D Shapes
- `triangle_area(base, height)` - Triangle area
- `triangle_area_heron(a, b, c)` - Triangle area (Heron's formula)
- `rectangle_area(length, width)` - Rectangle area
- `circle_area(radius)` - Circle area and circumference
- `circle_area_diameter(diameter)` - Circle from diameter
- `parallelogram_area(base, height)` - Parallelogram area
- `trapezoid_area(base1, base2, height)` - Trapezoid area
- `ellipse_area(semi_major, semi_minor)` - Ellipse area

#### 3D Shapes
- `sphere_volume(radius)` - Sphere volume & surface area
- `cube_volume(side)` - Cube volume & surface area
- `rectangular_prism_volume(length, width, height)` - Box volume
- `cylinder_volume(radius, height)` - Cylinder volume
- `cone_volume(radius, height)` - Cone volume
- `pyramid_volume(base_area, height)` - Pyramid volume

#### Geometric Calculations
- `pythagorean_theorem(a, b)` - Calculate hypotenuse
- `polygon_area(sides, side_length)` - Regular polygon area
- `distance_3d(x1, y1, z1, x2, y2, z2)` - 3D distance
- `GeometryCalculator` - Class with all methods

### Calculus Module (20+ Functions)

#### Derivatives
- `derivative_power_rule(coeff, exp)` - d/dx(cx^n)
- `derivative_sum_of_terms(coefficients, exponents)` - Polynomial derivative
- `second_derivative_power_rule(coeff, exp)` - Second derivative

#### Integrals
- `integral_power_rule(coeff, exp)` - ∫cx^n dx
- `definite_integral_polynomial(coefficients, exponents, a, b)` - Area under curve

#### Limits & Critical Points
- `limit_polynomial(coefficients, exponents, x_value)` - Polynomial limit
- `critical_points_quadratic(a, b, c)` - Find critical points

#### Numerical Methods
- `numerical_derivative(func, x)` - Numerical differentiation
- `rate_of_change(f_x2, f_x1, x2, x1)` - Average rate of change
- `CalculusSolver` - Class with all methods

### Statistics Module (20+ Functions)

#### Measures of Central Tendency
- `mean(data)` - Arithmetic mean
- `median(data)` - Middle value
- `mode(data)` - Most frequent value

#### Measures of Spread
- `range(data)` - Max - Min
- `variance(data, sample=False)` - Population/sample variance
- `standard_deviation(data, sample=False)` - Standard deviation
- `quartiles(data)` - Q1, Q2, Q3, IQR

#### Correlation & Regression
- `z_score(value, mean, std_dev)` - Standardized score
- `correlation_coefficient(x_data, y_data)` - Pearson correlation
- `linear_regression(x_data, y_data)` - Line of best fit
- `StatisticsCalculator` - Class with all methods

### Learning Module (Interactive)

#### Learning Tools
- `learn(topic)` - Get lessons with explanations
- `quiz(topic)` - Take interactive quizzes
- `practice(topic, difficulty)` - Get practice problems
- `tips(topic)` - Study tips and strategies

#### Supported Topics
- quadratic_equations
- pythagorean_theorem
- linear_equations
- quadratic_functions

#### Quizzes Available
- algebra
- geometry
- arithmetic

## Output Format

All solver functions return dictionaries with:

```python
{
    'result': <actual answer>,
    'steps': [<step 1>, <step 2>, ...],
    'formula': '<formatted formula>',
    <other relevant fields>
}
```

## Example: Quadratic Equation Solution

```python
result = mm.solve_quadratic(1, -5, 6)

print(result['result'])  # [3, 2]
print(result['steps'])
# Output:
# [
#   "Equation: x² - 5x + 6 = 0",
#   "Using quadratic formula: x = (-b ± √(b²-4ac)) / 2a",
#   "a = 1, b = -5, c = 6",
#   "Discriminant (Δ) = (-5)² - 4(1)(6) = 1",
#   "√Δ = √1 = 1",
#   "x₁ = (5 + 1) / 2 = 3",
#   "x₂ = (5 - 1) / 2 = 2",
#   "There are two solutions"
# ]
```

## Performance Notes

- All functions use Python's standard library
- No external dependencies required
- Suitable for educational use
- Handles edge cases (division by zero, negative roots, etc.)
- Provides clear error messages

## Best Practices

1. **Always check returned steps** - They provide learning value
2. **Use detailed solvers** - Get full explanations with `SolverClass.method()`
3. **Take quizzes** - Test your understanding
4. **Review lessons** - Before starting new topics
5. **Use practice mode** - Build confidence with problems

## Version Information

- **Current Version**: 1.0.0
- **Python Required**: 3.8+
- **Status**: Production Ready
- **License**: MIT

For updates and new features, visit: https://github.com/mathmentor/mathmentor
