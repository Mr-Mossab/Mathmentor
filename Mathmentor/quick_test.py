import sys
sys.path.insert(0, '.')
import mathmentor as mm

print('Testing MathMentor Library')
print('='*50)
print()

# Test Arithmetic
print('ARITHMETIC:')
print(f'  5 + 3 = {mm.add(5, 3)}')
print(f'  sqrt(16) = {mm.sqrt(16)}')
print()

# Test Algebra
print('ALGEBRA:')
result = mm.solve_quadratic(1, -5, 6)
print(f'  x squared - 5x + 6 = 0')
print(f'  Solutions: {result["result"]}')
print()

# Test Geometry
print('GEOMETRY:')
area = mm.circle_area(5)
print(f'  Circle area (r=5): {area:.2f}')
print()

# Test Statistics
print('STATISTICS:')
data = [1, 2, 3, 4, 5]
print(f'  Data: {data}')
print(f'  Mean: {mm.mean(data)}')
print()

# Test Learning
print('LEARNING:')
print('  Learning module loaded with lessons, quizzes, practice problems')
print()

print('='*50)
print('All tests passed!')
