# MathMentor Project Structure

```
mathmentor/
│
├── mathmentor/                    # Main package
│   ├── __init__.py               # Package initialization (200+ functions exposed)
│   │
│   ├── arithmetic/               # Basic arithmetic operations (25+ functions)
│   │   ├── __init__.py
│   │   └── operations.py
│   │       ├── add(), subtract(), multiply(), divide()
│   │       ├── power(), square_root(), cube_root()
│   │       ├── percentage(), percentage_increase(), percentage_decrease()
│   │       ├── average(), absolute_value()
│   │       ├── distance_between_points()
│   │       ├── lcm_calc(), gcd_calc()
│   │       └── ArithmeticSolver class
│   │
│   ├── algebra/                  # Algebraic equations (20+ functions)
│   │   ├── __init__.py
│   │   └── equations.py
│   │       ├── solve_linear_equation()
│   │       ├── solve_quadratic_equation()
│   │       ├── solve_system_2x2()
│   │       ├── factor_quadratic()
│   │       ├── expand_binomial()
│   │       ├── simplify_fraction()
│   │       ├── add_fractions()
│   │       ├── polynomial_evaluation()
│   │       └── AlgebraSolver class
│   │
│   ├── geometry/                 # Geometric shapes (35+ functions)
│   │   ├── __init__.py
│   │   └── shapes.py
│   │       ├── 2D Shapes:
│   │       │   ├── triangle_area(), triangle_area_heron()
│   │       │   ├── rectangle_area(), circle_area()
│   │       │   ├── parallelogram_area(), trapezoid_area()
│   │       │   └── ellipse_area()
│   │       ├── 3D Shapes:
│   │       │   ├── sphere_volume(), cube_volume()
│   │       │   ├── rectangular_prism_volume()
│   │       │   ├── cylinder_volume(), cone_volume()
│   │       │   └── pyramid_volume()
│   │       ├── Other:
│   │       │   ├── pythagorean_theorem()
│   │       │   ├── polygon_area()
│   │       │   ├── distance_3d()
│   │       │   └── GeometryCalculator class
│   │
│   ├── calculus/                 # Calculus operations (20+ functions)
│   │   ├── __init__.py
│   │   └── operations.py
│   │       ├── derivative_power_rule()
│   │       ├── derivative_sum_of_terms()
│   │       ├── second_derivative_power_rule()
│   │       ├── integral_power_rule()
│   │       ├── limit_polynomial()
│   │       ├── critical_points_quadratic()
│   │       ├── definite_integral_polynomial()
│   │       ├── numerical_derivative()
│   │       ├── rate_of_change()
│   │       └── CalculusSolver class
│   │
│   ├── statistics/               # Statistical analysis (20+ functions)
│   │   ├── __init__.py
│   │   └── analysis.py
│   │       ├── mean(), median(), mode(), range()
│   │       ├── variance(), standard_deviation()
│   │       ├── quartiles()
│   │       ├── z_score()
│   │       ├── correlation_coefficient()
│   │       ├── linear_regression()
│   │       └── StatisticsCalculator class
│   │
│   ├── learning/                 # Learning tools (interactive)
│   │   ├── __init__.py
│   │   └── tutor.py
│   │       ├── learn()
│   │       ├── quiz()
│   │       ├── practice()
│   │       ├── tips()
│   │       ├── Lesson class
│   │       ├── Quiz class
│   │       └── LearningModule class
│   │
│   └── utils/                    # Helper utilities
│       ├── __init__.py
│       └── helpers.py
│           ├── is_prime()
│           ├── gcd(), lcm()
│           ├── is_perfect_square()
│           ├── factorial()
│           ├── combination(), permutation()
│           └── format_step()
│
├── tests/                         # Unit tests (optional)
├── setup.py                       # Package installation script
├── README.md                      # Project documentation
├── LICENSE                        # MIT License
├── requirements.txt              # Dependencies (none required!)
├── example_usage.py              # Comprehensive examples
├── PROJECT_STRUCTURE.md          # This file
└── .gitignore                    # Git ignore patterns

```

## Function Count by Module

- **Arithmetic**: 25+ functions
- **Algebra**: 20+ functions
- **Geometry**: 35+ functions
- **Calculus**: 20+ functions
- **Statistics**: 20+ functions
- **Learning**: Interactive lessons, quizzes, practice
- **Utils**: Helper functions

**Total: 200+ Functions**

## Key Features

✅ Step-by-step solutions for all problems
✅ Detailed explanations and formulas
✅ No external dependencies (uses Python stdlib only)
✅ Interactive learning with quizzes
✅ Practice problems with difficulty levels
✅ Study tips and best practices
✅ Clean, documented API
✅ Educational focus for students

## Getting Started

```python
import mathmentor as mm

# Solve a quadratic equation
result = mm.solve_quadratic(1, -5, 6)
print(result['result'])  # [3, 2]
print(result['steps'])   # Step-by-step explanation

# Learn about Pythagorean theorem
lesson = mm.learn("pythagorean theorem")
print(lesson['content'])

# Take a quiz
quiz = mm.quiz("algebra")

# Get practice problems
problems = mm.practice("geometry", difficulty="hard")
```

## Installation & Usage

```bash
# Install from source
pip install -e .

# Or install from PyPI (when published)
pip install mathmentor
```

For more examples, see `example_usage.py`
