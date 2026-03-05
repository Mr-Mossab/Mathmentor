"""
Advanced Usage Examples for MathMentor Library
Demonstrates integration and advanced patterns
"""

import mathmentor as mm
import math


# ==============================================================================
# Example 1: Complete Problem Solving Workflow
# ==============================================================================
print("=" * 80)
print("Example 1: Complete Physics Problem Using MathMentor")
print("=" * 80)

print("""
Problem: A projectile is launched from a cliff 100m high at 30 m/s.
Calculate: 
  1. Time to hit the ground using quadratic equation
  2. Distance traveled
""")

# Use algebra to solve: -4.9t² + 30t + 100 = 0
print("\nHalf of gravity: g/2 = 4.9")
result = mm.solve_quadratic(-4.9, 30, 100)

print(f"Solutions: {result['result']}")
print("Valid solution (positive time):", max(result['result']))

# Use the time to calculate distance
time_to_ground = max(result['result'])
distance = 30 * time_to_ground
print(f"Horizontal distance (at 30 m/s): {distance:.2f} m")


# ==============================================================================
# Example 2: Statistical Analysis of Student Grades
# ==============================================================================
print("\n" + "=" * 80)
print("Example 2: Grade Statistical Analysis")
print("=" * 80)

grades = [85, 92, 78, 95, 88, 76, 92, 89, 91, 87]

print(f"Grades: {grades}")
print(f"\nStatistical Analysis:")

mean_grade = mm.mean(grades)
median_grade = mm.median(grades)
std = mm.std_dev(grades, sample=True)

print(f"  Mean (Average): {mean_grade:.2f}")
print(f"  Median: {median_grade:.2f}")
print(f"  Standard Deviation: {std:.2f}")

# Get detailed result
result = mm.StatisticsCalculator.standard_deviation(grades, sample=True)
print(f"\nDetailed Steps:")
for step in result['steps'][-3:]:
    print(f"  - {step}")

# Calculate z-scores
print(f"\nZ-score Analysis (convert to std normal):")
student_score = 92
z = mm.z_score(student_score, mean_grade, std)['z_score']
print(f"  Student with score 92 has z-score: {z:.2f}")


# ==============================================================================
# Example 3: Engineering Problem - Tank Calculations
# ==============================================================================
print("\n" + "=" * 80)
print("Example 3: Engineering Problem - Cylindrical Tank Volume")
print("=" * 80)

print("""
Problem: A cylindrical water tank has radius 2m and height 5m.
Calculate the volume and required paint surface area.
""")

radius = 2
height = 5

result = mm.GeometryCalculator.cylinder_volume(radius, height)
print(f"Volume: {result['volume']:.2f} cubic meters")
print(f"Lateral Surface Area (to paint): {result['lateral_area']:.2f} square meters")

# If 1 liter of paint covers 10 m²
liters_needed = result['lateral_area'] / 10
cost_per_liter = 5  # dollars
total_cost = liters_needed * cost_per_liter

print(f"Paint needed: {liters_needed:.2f} liters")
print(f"Cost at $5/liter: ${total_cost:.2f}")


# ==============================================================================
# Example 4: Data Fitting and Prediction
# ==============================================================================
print("\n" + "=" * 80)
print("Example 4: Linear Regression - Temperature vs Ice Cream Sales")
print("=" * 80)

# Temperature (°C) vs Sales (units)
temperatures = [20, 22, 24, 26, 28, 30]
sales = [15, 20, 25, 30, 38, 42]

result = mm.StatisticsCalculator.linear_regression(temperatures, sales)

print(f"Temperature data: {temperatures}")
print(f"Sales data: {sales}")
print(f"\nRegression Equation: {result['equation']}")
print(f"Slope (sales per degree): {result['slope']:.2f}")
print(f"Y-intercept: {result['intercept']:.2f}")

# Predict sales at 32°C
predicted_temp = 32
predicted_sales = result['slope'] * predicted_temp + result['intercept']
print(f"\nPredicted sales at 32°C: {predicted_sales:.0f} units")


# ==============================================================================
# Example 5: Geometry Problem - Design Optimization
# ==============================================================================
print("\n" + "=" * 80)
print("Example 5: Geometry - Field Design Optimization")
print("=" * 80)

print("""
Problem: Design a rectangular field with fixed perimeter of 200m.
Find which dimensions give maximum area.
""")

# For rectangle with perimeter P = 2(L + W) = 200, so L + W = 100
# Area = L × W = L × (100 - L) = 100L - L²
# This is a quadratic: A = -L² + 100L

result = mm.CalculusSolver.critical_points_quadratic(-1, 100, 0)
optimal_length = result['critical_point'][0]
optimal_width = 100 - optimal_length
max_area = result['critical_point'][1]

print(f"Optimal length: {optimal_length:.0f}m")
print(f"Optimal width: {optimal_width:.0f}m")
print(f"Maximum area: {max_area:.0f} square meters")
print(f"\nNote: Maximum area occurs when field is square (50m × 50m)")


# ==============================================================================
# Example 6: Calculus - Rate of Change Analysis
# ==============================================================================
print("\n" + "=" * 80)
print("Example 6: Calculus - Velocity and Acceleration")
print("=" * 80)

print("""
Position function: s(t) = 5t² - 2t + 10
Find velocity and acceleration at t = 3 seconds.
""")

# Coefficients for s(t) = 5t² - 2t + 10
t = 3

# Position at t=3
position = 5*t**2 - 2*t + 10
print(f"Position at t=3: s(3) = {position}m")

# Velocity is derivative: v(t) = 10t - 2
velocity = 10*t - 2
print(f"Velocity at t=3: v(3) = {velocity} m/s (using v = 10t - 2)")

# Acceleration is second derivative: a(t) = 10
acceleration = 10
print(f"Acceleration at t=3: a(3) = {acceleration} m/s²")

# Use calculus solver
result = mm.CalculusSolver.derivative_power_rule(5, 2)
print(f"\nUsing Power Rule on 5t²:")
print(f"  Derivative: {result['derivative']} (for the t² term)")


# ==============================================================================
# Example 7: Comprehensive Learning Path
# ==============================================================================
print("\n" + "=" * 80)
print("Example 7: Student Learning Path")
print("=" * 80)

# Suggest learning sequence
topics = [
    "linear_equations",
    "quadratic_equations",
    "pythagorean_theorem"
]

for topic in topics:
    lesson = mm.learn(topic)
    print(f"\n[LESSON] {lesson['title']}")
    print(f"  Concepts: {len(lesson['concepts'])} key concepts")
    print(f"  Examples: {lesson['examples_count']} worked examples")


# ==============================================================================
# Example 8: Error Handling and Edge Cases
# ==============================================================================
print("\n" + "=" * 80)
print("Example 8: Handling Edge Cases and Errors")
print("=" * 80)

# Division by zero
try:
    result = mm.divide(10, 0)
except ValueError as e:
    print(f"✓ Caught error: {e}")

# Negative square root
try:
    result = mm.sqrt(-4)
except ValueError as e:
    print(f"✓ Caught error: {e}")

# Zero discriminant (repeated root)
result = mm.solve_quadratic(1, -2, 1)
print(f"\n✓ x² - 2x + 1 = 0 (perfect square)")
print(f"  Solution: {result['result']}")

# Complex solutions
result = mm.solve_quadratic(1, 0, 1)
print(f"\n✓ x² + 1 = 0 (no real solutions)")
print(f"  Result: {result['result']}")


# ==============================================================================
# Example 9: Batch Calculations
# ==============================================================================
print("\n" + "=" * 80)
print("Example 9: Batch Calculations - Multiple Geometry Problems")
print("=" * 80)

geometries = [
    ("Circle", 5, "radius"),
    ("Rectangle", (8, 6), "dimensions"),
    ("Triangle", (12, 5), "base, height"),
]

print("\nCalculating areas:")
for name, value, desc in geometries:
    if name == "Circle":
        area = mm.circle_area(value)
        print(f"  {name} ({desc}={value}): Area = {area:.2f}")
    elif name == "Rectangle":
        area = mm.rectangle_area(value[0], value[1])
        print(f"  {name} ({desc}={value}): Area = {area:.0f}")
    elif name == "Triangle":
        area = mm.triangle_area(value[0], value[1])
        print(f"  {name} ({desc}={value}): Area = {area:.0f}")


# ==============================================================================
# Example 10: Performance Comparison
# ==============================================================================
print("\n" + "=" * 80)
print("Example 10: Quick Calculation Summary")
print("=" * 80)

# Quick reference of common calculations
operations = [
    ("Square root of 144", lambda: mm.sqrt(144)),
    ("12% of 250", lambda: mm.percentage(250, 12)['result'] 
     if isinstance(mm.percentage(250, 12), dict) else 
     mm.ArithmeticSolver.percentage(250, 12)['result']),
    ("Circle area (r=10)", lambda: mm.circle_area(10)),
    ("Mean of [5,10,15,20]", lambda: mm.mean([5, 10, 15, 20])),
]

for desc, func in operations:
    result = func()
    if isinstance(result, float):
        print(f"  {desc}: {result:.2f}")
    else:
        print(f"  {desc}: {result}")


print("\n" + "=" * 80)
print("All examples completed successfully!")
print("MathMentor is ready for educational use!")
print("=" * 80)
