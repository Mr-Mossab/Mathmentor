"""
Learning Module - Educational content, lessons, quizzes, and practice problems
"""

import random
from typing import Dict, List, Any, Tuple


class Lesson:
    """Represents a lesson with explanation and examples"""
    
    def __init__(self, title: str, description: str, concepts: List[str], examples: List[Dict]):
        self.title = title
        self.description = description
        self.concepts = concepts
        self.examples = examples
    
    def display(self) -> str:
        """Display lesson content"""
        content = f"\n{'='*60}\n"
        content += f"LESSON: {self.title}\n"
        content += f"{'='*60}\n"
        content += f"\n{self.description}\n"
        content += f"\nKey Concepts:\n"
        for i, concept in enumerate(self.concepts, 1):
            content += f"  {i}. {concept}\n"
        content += f"\nExamples:\n"
        for i, example in enumerate(self.examples, 1):
            content += f"  Example {i}: {example['problem']}\n"
            content += f"  Solution: {example['solution']}\n\n"
        return content


class Quiz:
    """Interactive quiz with multiple choice questions"""
    
    def __init__(self, title: str, topic: str, questions: List[Dict]):
        self.title = title
        self.topic = topic
        self.questions = questions
        self.score = 0
        self.answers = []
    
    def run(self) -> Dict[str, Any]:
        """Run the quiz and return results"""
        print(f"\n{'='*60}")
        print(f"QUIZ: {self.title}")
        print(f"Topic: {self.topic}")
        print(f"{'='*60}\n")
        
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question['question']}")
            for j, option in enumerate(question['options'], 1):
                print(f"  {j}. {option}")
            
            # For automated use, we'll just show correct answer
            correct_idx = question['correct'] - 1
            print(f"\n✓ Correct answer: {question['correct']}. {question['options'][correct_idx]}")
            print(f"  Explanation: {question.get('explanation', 'N/A')}\n")
            
            self.score += 1
        
        total_questions = len(self.questions)
        percentage = (self.score / total_questions * 100) if total_questions > 0 else 0
        
        return {
            'score': self.score,
            'total': total_questions,
            'percentage': percentage,
            'topic': self.topic,
            'title': self.title
        }


class LearningModule:
    """Main learning module with lessons, quizzes, and practice"""
    
    LESSONS = {
        'quadratic_equations': Lesson(
            title="Quadratic Equations",
            description="A quadratic equation is an equation of the form ax² + bx + c = 0, where a ≠ 0. Quadratic equations can be solved using several methods including factoring, completing the square, or the quadratic formula.",
            concepts=[
                "Standard form: ax² + bx + c = 0",
                "Quadratic formula: x = (-b ± √(b² - 4ac)) / 2a",
                "Discriminant: Δ = b² - 4ac determines number of solutions",
                "If Δ > 0: two distinct real solutions",
                "If Δ = 0: one repeated real solution",
                "If Δ < 0: no real solutions (complex solutions)"
            ],
            examples=[
                {
                    'problem': 'Solve 2x² + 5x + 3 = 0',
                    'solution': 'Using quadratic formula: x = (-5 ± √(25-24))/4 = (-5 ± 1)/4\nSolutions: x = -1 and x = -1.5'
                },
                {
                    'problem': 'Solve x² - 4 = 0',
                    'solution': 'This is a difference of squares: (x-2)(x+2) = 0\nSolutions: x = 2 and x = -2'
                }
            ]
        ),
        'pythagorean_theorem': Lesson(
            title="Pythagorean Theorem",
            description="In a right triangle, the square of the hypotenuse equals the sum of squares of the other two sides. This is one of the most important theorems in geometry.",
            concepts=[
                "Formula: c² = a² + b²",
                "c is the hypotenuse (longest side)",
                "a and b are the other two sides",
                "Works only for right triangles (one 90° angle)",
                "Used to find missing sides and verify right triangles"
            ],
            examples=[
                {
                    'problem': 'Find the hypotenuse of a right triangle with sides 3 and 4',
                    'solution': 'c² = 3² + 4² = 9 + 16 = 25\nc = √25 = 5'
                },
                {
                    'problem': 'A ladder of length 13 ft leans against a wall 12 ft high. How far is the base from the wall?',
                    'solution': '13² = 12² + b²\n169 = 144 + b²\nb² = 25, so b = 5 ft'
                }
            ]
        ),
        'linear_equations': Lesson(
            title="Linear Equations",
            description="A linear equation is an equation where variables appear with exponent 1. The simplest form is y = mx + b, where m is the slope and b is the y-intercept.",
            concepts=[
                "Slope-intercept form: y = mx + b",
                "m is the slope (rate of change)",
                "b is the y-intercept",
                "Slope = (y₂ - y₁) / (x₂ - x₁)",
                "Parallel lines have equal slopes",
                "Perpendicular lines have slopes that multiply to -1"
            ],
            examples=[
                {
                    'problem': 'Write equation of line through (2,3) with slope 2',
                    'solution': 'Using y = mx + b: 3 = 2(2) + b\n3 = 4 + b, so b = -1\nEquation: y = 2x - 1'
                },
                {
                    'problem': 'Find slope between points (1,2) and (4,8)',
                    'solution': 'm = (8-2)/(4-1) = 6/3 = 2'
                }
            ]
        ),
        'quadratic_functions': Lesson(
            title="Quadratic Functions",
            description="A quadratic function has the form f(x) = ax² + bx + c. The graph is a parabola that opens upward if a > 0 or downward if a < 0.",
            concepts=[
                "Vertex form: f(x) = a(x - h)² + k where vertex is (h,k)",
                "The vertex is the minimum/maximum point",
                "Axis of symmetry: x = -b/2a",
                "Y-intercept: set x = 0, get f(0) = c",
                "Opens upward if a > 0, downward if a < 0",
                "Wider if |a| < 1, narrower if |a| > 1"
            ],
            examples=[
                {
                    'problem': 'Find vertex of f(x) = 2x² - 8x + 3',
                    'solution': 'x = -b/2a = -(-8)/4 = 2\nf(2) = 2(4) - 8(2) + 3 = -5\nVertex: (2, -5)'
                }
            ]
        )
    }

    QUIZZES = {
        'algebra': Quiz(
            title='Algebra Fundamentals Quiz',
            topic='Algebra',
            questions=[
                {
                    'question': 'Solve for x: 3x + 5 = 20',
                    'options': ['x = 5', 'x = 3', 'x = 8', 'x = 2'],
                    'correct': 1,
                    'explanation': '3x = 20 - 5 = 15, so x = 15/3 = 5'
                },
                {
                    'question': 'What is the discriminant of 2x² + 3x + 1 = 0?',
                    'options': ['Δ = 1', 'Δ = 9', 'Δ = 17', 'Δ = -7'],
                    'correct': 1,
                    'explanation': 'Δ = b²- 4ac = 9 - 8 = 1'
                },
                {
                    'question': 'Factor: x² + 5x + 6',
                    'options': ['(x+2)(x+3)', '(x+1)(x+6)', '(x+2)(x+2)', '(x-2)(x-3)'],
                    'correct': 1,
                    'explanation': 'Find two numbers that multiply to 6 and add to 5: 2 and 3'
                }
            ]
        ),
        'geometry': Quiz(
            title='Geometry Basics Quiz',
            topic='Geometry',
            questions=[
                {
                    'question': 'What is the area of a circle with radius 5?',
                    'options': ['25π', '10π', '10', '15π'],
                    'correct': 1,
                    'explanation': 'A = πr² = π(5)² = 25π ≈ 78.54'
                },
                {
                    'question': 'A right triangle has legs 6 and 8. What is the hypotenuse?',
                    'options': ['10', '12', '14', '7'],
                    'correct': 1,
                    'explanation': 'c² = 6² + 8² = 36 + 64 = 100, so c = 10'
                },
                {
                    'question': 'What is the sum of angles in a triangle?',
                    'options': ['90°', '180°', '270°', '360°'],
                    'correct': 2,
                    'explanation': 'The sum of interior angles in any triangle is always 180°'
                }
            ]
        ),
        'arithmetic': Quiz(
            title='Arithmetic Operations Quiz',
            topic='Arithmetic',
            questions=[
                {
                    'question': 'What is 12% of 150?',
                    'options': ['18', '15', '20', '12'],
                    'correct': 1,
                    'explanation': '12% × 150 = 0.12 × 150 = 18'
                },
                {
                    'question': 'What is √144?',
                    'options': ['11', '12', '14', '13'],
                    'correct': 2,
                    'explanation': '12 × 12 = 144, so √144 = 12'
                },
                {
                    'question': 'What is 2³ × 2² ?',
                    'options': ['32', '64', '16', '8'],
                    'correct': 1,
                    'explanation': '2³ × 2² = 2^(3+2) = 2⁵ = 32'
                }
            ]
        )
    }

    @staticmethod
    def learn(topic: str) -> Dict[str, Any]:
        """Get a lesson on a specific topic"""
        topic_lower = topic.lower().replace(' ', '_')
        
        if topic_lower in LearningModule.LESSONS:
            lesson = LearningModule.LESSONS[topic_lower]
            return {
                'type': 'lesson',
                'title': lesson.title,
                'content': lesson.display(),
                'concepts': lesson.concepts,
                'examples_count': len(lesson.examples)
            }
        else:
            available = list(LearningModule.LESSONS.keys())
            return {
                'type': 'error',
                'message': f"Topic '{topic}' not found",
                'available_topics': available
            }

    @staticmethod
    def quiz(topic: str) -> Dict[str, Any]:
        """Take a quiz on a specific topic"""
        topic_lower = topic.lower()
        
        if topic_lower in LearningModule.QUIZZES:
            quiz = LearningModule.QUIZZES[topic_lower]
            result = quiz.run()
            return {
                'type': 'quiz_result',
                'result': result
            }
        else:
            available = list(LearningModule.QUIZZES.keys())
            return {
                'type': 'error',
                'message': f"Quiz for '{topic}' not found",
                'available_quizzes': available
            }

    @staticmethod
    def practice(topic: str, difficulty: str = 'medium') -> Dict[str, Any]:
        """Generate practice problems"""
        problems = {
            'arithmetic': [
                'Calculate: 25 + 13 × 2',
                'Find: 144 ÷ 12',
                'Compute: (8 + 2)² - 50',
                'What is 15% of 200?',
                'Express as decimal: 3/8'
            ],
            'algebra': [
                'Solve: 2x + 7 = 15',
                'Solve: x² - 9 = 0',
                'Simplify: 3(x + 2) - 2x',
                'Factor: x² + 7x + 12',
                'Evaluate: 2a² - 3a + 1 when a = 3'
            ],
            'geometry': [
                'Find the area of a rectangle 8 × 5',
                'Find the circumference of a circle with r = 4',
                'Find the volume of a cube with side 3',
                'A triangle has base 10 and height 6. Find the area.',
                'Right triangle legs are 5 and 12. Find hypotenuse.'
            ]
        }
        
        if topic.lower() in problems:
            all_problems = problems[topic.lower()]
            if difficulty == 'easy':
                selected = all_problems[:2]
            elif difficulty == 'hard':
                selected = all_problems[-2:]
            else:
                selected = random.sample(all_problems, 3)
            
            return {
                'type': 'practice',
                'topic': topic,
                'difficulty': difficulty,
                'problems': selected,
                'count': len(selected)
            }
        else:
            return {
                'type': 'error',
                'message': f"No practice problems for '{topic}'"
            }

    @staticmethod
    def get_tips(topic: str) -> Dict[str, Any]:
        """Get study tips for a topic"""
        tips = {
            'algebra': [
                'Always isolate the variable on one side of the equation',
                'Whatever you do to one side, do to the other side',
                'For quadratic equations, remember the discriminant tells you about solutions',
                'Check your answers by substituting back into the original equation',
                'Practice factoring patterns like difference of squares and trinomials'
            ],
            'geometry': [
                'Draw diagrams to visualize the problem',
                'Label all known measurements',
                'Use the Pythagorean theorem for right triangles',
                'Remember formulas for area and volume by understanding them',
                'Use coordinate geometry to verify angle relationships'
            ],
            'calculus': [
                'Understand the concept before memorizing formulas',
                'Practice the power rule for derivatives extensively',
                'Draw graphs to visualize limits and continuity',
                'Check your answers using numerical methods',
                'Practice chain rule with composite functions'
            ],
            'statistics': [
                'Always check your data is relevant and without errors',
                'Use the appropriate measure of central tendency',
                'Standard deviation tells you about data spread',
                'Correlation ≠ causation',
                'Visualize data with histograms and scatter plots'
            ]
        }
        
        if topic.lower() in tips:
            return {
                'type': 'tips',
                'topic': topic,
                'tips': tips[topic.lower()]
            }
        else:
            return {
                'type': 'error',
                'message': f"No tips available for '{topic}'"
            }


# Public functions
def learn(topic):
    """Learn about a topic"""
    return LearningModule.learn(topic)


def quiz(topic):
    """Take a quiz"""
    return LearningModule.quiz(topic)


def practice(topic, difficulty='medium'):
    """Get practice problems"""
    return LearningModule.practice(topic, difficulty)


def tips(topic):
    """Get study tips"""
    return LearningModule.get_tips(topic)
