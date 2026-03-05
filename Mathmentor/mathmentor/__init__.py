"""
MathMentor - Interactive Mathematics Learning Library
A comprehensive Python library for learning mathematics with step-by-step solutions and explanations.

Version: 1.0.0
Author: Mossab
License: MIT

Features:
- Arithmetic operations (basic to advanced)
- Algebraic equations and expressions
- Geometric shapes and calculations
- Calculus (derivatives, integrals, limits)
- Statistical analysis
- Interactive learning with quizzes and practice problems

Usage:
    import mathmentor
    
    # Arithmetic
    result = mathmentor.arithmetic.sqrt(16)
    
    # Algebra
    solution = mathmentor.algebra.solve_quadratic(1, -5, 6)
    
    # Geometry
    area = mathmentor.geometry.circle_area(5)
    
    # Statistics
    mean_val = mathmentor.statistics.mean([1, 2, 3, 4, 5])
    
    # Learning
    lesson = mathmentor.learning.learn("quadratic equations")
    quiz_result = mathmentor.learning.quiz("algebra")
"""

__version__ = "1.0.0"
__author__ = "MathMentor Contributors"
__license__ = "MIT"

# Import main modules
from . import arithmetic
from . import algebra
from . import geometry
from . import calculus
from . import statistics
from . import learning
from . import utils

# Expose main functions at package level for easier access
from .arithmetic import (
    add, subtract, multiply, divide, power, sqrt, cbrt,
    ArithmeticSolver
)

from .algebra import (
    solve_linear, solve_quadratic,
    AlgebraSolver
)

from .geometry import (
    triangle_area, circle_area, sphere_volume, cube_volume,
    GeometryCalculator
)

from .statistics import (
    mean, median, mode, std_dev,
    StatisticsCalculator
)

from .learning import (
    learn, quiz, practice, tips,
    LearningModule
)

__all__ = [
    # Modules
    'arithmetic',
    'algebra',
    'geometry',
    'calculus',
    'statistics',
    'learning',
    'utils',
    
    # Arithmetic functions
    'add',
    'subtract',
    'multiply',
    'divide',
    'power',
    'sqrt',
    'cbrt',
    'ArithmeticSolver',
    
    # Algebra functions
    'solve_linear',
    'solve_quadratic',
    'AlgebraSolver',
    
    # Geometry functions
    'triangle_area',
    'circle_area',
    'sphere_volume',
    'cube_volume',
    'GeometryCalculator',
    
    # Statistics functions
    'mean',
    'median',
    'mode',
    'std_dev',
    'StatisticsCalculator',
    
    # Learning functions
    'learn',
    'quiz',
    'practice',
    'tips',
    'LearningModule'
]


def get_version():
    """Get the version of MathMentor"""
    return __version__


def get_info():
    """Get information about MathMentor"""
    return {
        'name': 'MathMentor',
        'version': __version__,
        'description': 'Interactive Mathematics Learning Library',
        'author': __author__,
        'license': __license__,
        'modules': [
            'arithmetic',
            'algebra',
            'geometry',
            'calculus',
            'statistics',
            'learning'
        ]
    }
