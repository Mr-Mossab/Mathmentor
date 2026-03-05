"""
Unit Tests for MathMentor Library
"""

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import mathmentor as mm


class TestArithmetic(unittest.TestCase):
    """Test Arithmetic Module"""
    
    def test_add(self):
        result = mm.add(5, 3)
        self.assertEqual(result, 8)
    
    def test_subtract(self):
        result = mm.subtract(10, 3)
        self.assertEqual(result, 7)
    
    def test_multiply(self):
        result = mm.multiply(4, 7)
        self.assertEqual(result, 28)
    
    def test_divide(self):
        result = mm.divide(20, 4)
        self.assertEqual(result, 5)
    
    def test_power(self):
        result = mm.power(2, 3)
        self.assertEqual(result, 8)
    
    def test_sqrt(self):
        result = mm.sqrt(16)
        self.assertEqual(result, 4)
    
    def test_sqrt_detailed(self):
        result = mm.ArithmeticSolver.square_root(25)
        self.assertEqual(result['result'], 5)
        self.assertIn('steps', result)
        self.assertIn('formula', result)


class TestAlgebra(unittest.TestCase):
    """Test Algebra Module"""
    
    def test_linear_equation(self):
        result = mm.solve_linear(2, 5, 13)
        self.assertEqual(result['result'], 4)
    
    def test_quadratic_equation(self):
        result = mm.solve_quadratic(1, -5, 6)
        solutions = sorted(result['result'])
        self.assertEqual(solutions, [2, 3])
    
    def test_quadratic_detailed(self):
        result = mm.AlgebraSolver.solve_quadratic_equation(1, -5, 6)
        self.assertIn('result', result)
        self.assertIn('steps', result)
        self.assertIn('formula', result)


class TestGeometry(unittest.TestCase):
    """Test Geometry Module"""
    
    def test_triangle_area(self):
        result = mm.triangle_area(8, 6)
        self.assertEqual(result, 24)
    
    def test_circle_area(self):
        import math
        result = mm.circle_area(5)
        expected = math.pi * 25
        self.assertAlmostEqual(result, expected, places=4)
    
    def test_sphere_volume(self):
        import math
        result = mm.sphere_volume(3)
        expected = (4/3) * math.pi * 27
        self.assertAlmostEqual(result, expected, places=4)
    
    def test_pythagorean_theorem(self):
        result = mm.GeometryCalculator.pythagorean_theorem(3, 4)
        self.assertEqual(result['hypotenuse'], 5)


class TestStatistics(unittest.TestCase):
    """Test Statistics Module"""
    
    def setUp(self):
        self.data = [1, 2, 3, 4, 5]
    
    def test_mean(self):
        result = mm.mean(self.data)
        self.assertEqual(result, 3)
    
    def test_median(self):
        result = mm.median(self.data)
        self.assertEqual(result, 3)
    
    def test_mode(self):
        data = [1, 2, 2, 3, 4]
        result = mm.mode(data)
        self.assertEqual(result, 2)
    
    def test_std_dev(self):
        result = mm.std_dev([10, 20, 30])
        self.assertGreater(result, 0)


class TestCalculus(unittest.TestCase):
    """Test Calculus Module"""
    
    def test_derivative_power_rule(self):
        result = mm.CalculusSolver.derivative_power_rule(3, 2)
        self.assertEqual(result['derivative'], '6x^1')
    
    def test_integral_power(self):
        result = mm.CalculusSolver.integral_power_rule(2, 1)
        self.assertIn('integral', result)


class TestLearning(unittest.TestCase):
    """Test Learning Module"""
    
    def test_learn_lesson(self):
        result = mm.learn("quadratic equations")
        self.assertEqual(result['type'], 'lesson')
        self.assertIn('content', result)
    
    def test_quiz_algebra(self):
        result = mm.quiz("algebra")
        self.assertEqual(result['type'], 'quiz_result')
    
    def test_practice(self):
        result = mm.practice("geometry", "medium")
        self.assertEqual(result['type'], 'practice')
        self.assertIn('problems', result)
    
    def test_tips(self):
        result = mm.tips("algebra")
        self.assertEqual(result['type'], 'tips')
        self.assertIn('tips', result)


class TestLibraryInfo(unittest.TestCase):
    """Test Library Information"""
    
    def test_get_version(self):
        version = mm.get_version()
        self.assertEqual(version, "1.0.0")
    
    def test_get_info(self):
        info = mm.get_info()
        self.assertEqual(info['name'], 'MathMentor')
        self.assertIn('modules', info)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)
