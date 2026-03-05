"""
Example usage of MathMentor library
Demonstrates all main modules and functions
"""

import mathmentor as mm

print("=" * 70)
print("MathMentor - Interactive Mathematics Learning Library")
print("=" * 70)

# ============================================================================
# ARITHMETIC MODULE
# ============================================================================
print("\n\n📊 ARITHMETIC MODULE")
print("-" * 70)

print("\n1. Basic Operations:")
print(f"   5 + 3 = {mm.add(5, 3)}")
print(f"   10 - 3 = {mm.subtract(10, 3)}")
print(f"   4 × 7 = {mm.multiply(4, 7)}")
print(f"   20 ÷ 4 = {mm.divide(20, 4)}")

print("\n2. Powers and Roots:")
print(f"   2³ = {mm.power(2, 3)}")
print(f"   √16 = {mm.sqrt(16)}")
print(f"   ³√27 = {mm.cbrt(27)}")

print("\n3. Detailed Solution:")
result = mm.ArithmeticSolver.square_root(25)
print(f"   Problem: √25")
print("   Steps:")
for step in result['steps']:
    print(f"   - {step}")

print("\n4. Percentage Calculations:")
result = mm.ArithmeticSolver.percentage(100, 20)
print(f"   20% of 100:")
for step in result['steps']:
    print(f"   - {step}")

print("\n5. Statistics:")
numbers = [1, 2, 3, 4, 5]
result = mm.ArithmeticSolver.average(numbers)
print(f"   Average of {numbers}:")
for step in result['steps'][:3]:
    print(f"   - {step}")
print(f"   Result: {result['result']}")

# ============================================================================
# ALGEBRA MODULE
# ============================================================================
print("\n\n🔡 ALGEBRA MODULE")
print("-" * 70)

print("\n1. Linear Equation: 2x + 5 = 13")
result = mm.AlgebraSolver.solve_linear_equation(2, 5, 13)
print(f"   Solution: x = {result['result']}")
print("   Steps:")
for step in result['steps']:
    print(f"   - {step}")

print("\n2. Quadratic Equation: x² - 5x + 6 = 0")
result = mm.solve_quadratic(1, -5, 6)
print(f"   Solutions: {result['result']}")
print("   Steps:")
for step in result['steps'][:5]:
    print(f"   - {step}")

print("\n3. Simplify Fraction: 12/18")
result = mm.AlgebraSolver.simplify_fraction(12, 18)
print(f"   Simplified: {result['result']}")
print(f"   Decimal: {result['decimal']:.4f}")

# ============================================================================
# GEOMETRY MODULE
# ============================================================================
print("\n\n📐 GEOMETRY MODULE")
print("-" * 70)

print("\n1. Circle Area (radius = 5):")
result = mm.GeometryCalculator.circle_area(5)
print(f"   Area: {result['area']:.4f}")
print(f"   Circumference: {result['circumference']:.4f}")

print("\n2. Triangle Area (base=8, height=6):")
result = mm.triangle_area(8, 6)
print(f"   Area: {result}")

print("\n3. Pythagorean Theorem (a=3, b=4):")
result = mm.GeometryCalculator.pythagorean_theorem(3, 4)
print(f"   Hypotenuse: {result['hypotenuse']}")
for step in result['steps']:
    print(f"   - {step}")

print("\n4. Sphere Volume (radius = 3):")
result = mm.sphere_volume(3)
print(f"   Volume: {result:.4f}")

print("\n5. Cube Volume (side = 5):")
result = mm.cube_volume(5)
print(f"   Volume: {result:.4f}")

# ============================================================================
# CALCULUS MODULE
# ============================================================================
print("\n\n📈 CALCULUS MODULE")
print("-" * 70)

print("\n1. Derivative of 3x²:")
result = mm.CalculusSolver.derivative_power_rule(3, 2)
print(f"   Derivative: {result['derivative']}")

print("\n2. Integral of 2x:")
result = mm.integral_power(2, 1)
print(f"   Integral: {result}")

print("\n3. Critical Points of f(x) = x² - 4x + 3:")
result = mm.CalculusSolver.critical_points_quadratic(1, -4, 3)
print(f"   Critical Point: {result['critical_point']}")
print(f"   Type: {result['type']}")

print("\n4. Rate of Change:")
result = mm.CalculusSolver.rate_of_change(8, 2, 4, 1)
print(f"   Rate: {result['rate']:.4f}")

# ============================================================================
# STATISTICS MODULE
# ============================================================================
print("\n\n📊 STATISTICS MODULE")
print("-" * 70)

data = [10, 20, 30, 40, 50]

print(f"\nData: {data}")

result = mm.StatisticsCalculator.mean(data)
print(f"\n1. Mean: {result['mean']}")

result = mm.StatisticsCalculator.median(data)
print(f"2. Median: {result['median']}")

result = mm.StatisticsCalculator.standard_deviation(data)
print(f"3. Standard Deviation: {result['std_dev']:.4f}")

result = mm.StatisticsCalculator.range(data)
print(f"4. Range: {result['range']}")

print("\n5. Quartiles:")
result = mm.StatisticsCalculator.quartiles(data)
print(f"   Q1: {result['Q1']}")
print(f"   Q2 (Median): {result['Q2']}")
print(f"   Q3: {result['Q3']}")
print(f"   IQR: {result['IQR']}")

# ============================================================================
# LEARNING MODULE
# ============================================================================
print("\n\n🎓 LEARNING MODULE")
print("-" * 70)

print("\n1. Available Learning Topics:")
topics = ['quadratic_equations', 'pythagorean_theorem', 'linear_equations', 'quadratic_functions']
for i, topic in enumerate(topics, 1):
    print(f"   {i}. {topic.replace('_', ' ').title()}")

print("\n2. Sample Quiz (Algebra):")
result = mm.learning.quiz("algebra")
print(f"   Quiz: {result['result']['title']}")
print(f"   Total Questions: {result['result']['total']}")

print("\n3. Practice Problems (Geometry):")
result = mm.practice("geometry", "medium")
print(f"   Topic: {result['topic']}")
print(f"   Difficulty: {result['difficulty']}")
print(f"   Problems:")
for i, prob in enumerate(result['problems'], 1):
    print(f"   {i}. {prob}")

print("\n4. Study Tips (Algebra):")
result = mm.tips("algebra")
print(f"   Topic: {result['topic']}")
print("   Tips:")
for i, tip in enumerate(result['tips'], 1):
    print(f"   {i}. {tip}")

# ============================================================================
# LIBRARY INFO
# ============================================================================
print("\n\n" + "=" * 70)
print("Library Information")
print("=" * 70)
info = mm.get_info()
print(f"Name: {info['name']}")
print(f"Version: {info['version']}")
print(f"Description: {info['description']}")
print(f"Modules: {', '.join(info['modules'])}")

print("\n" + "=" * 70)
print("For more information, visit: https://github.com/mathmentor/mathmentor")
print("=" * 70)
