"""
Geometry Module - Shapes, areas, volumes, angles, and geometric calculations
"""

import math
from typing import Dict, Any, Union
from ..utils.helpers import round_to_decimal


class GeometryCalculator:
    """Calculates geometric properties with step-by-step explanations"""

    # ------ 2D Shapes ------

    @staticmethod
    def triangle_area(base: float, height: float) -> Dict[str, Any]:
        """Calculate area of a triangle"""
        area = (base * height) / 2
        steps = [
            f"Triangle area calculation",
            f"Base = {base}, Height = {height}",
            f"Formula: Area = (base × height) / 2",
            f"Area = ({base} × {height}) / 2 = {round_to_decimal(area, 4)}"
        ]
        return {
            'area': area,
            'steps': steps,
            'formula': f'Area = {round_to_decimal(area, 4)} square units'
        }

    @staticmethod
    def triangle_area_heron(a: float, b: float, c: float) -> Dict[str, Any]:
        """Calculate triangle area using Heron's formula"""
        s = (a + b + c) / 2  # semi-perimeter
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        steps = [
            f"Triangle with sides: a={a}, b={b}, c={c}",
            f"Using Heron's formula:",
            f"Semi-perimeter s = (a + b + c) / 2 = ({a} + {b} + {c}) / 2 = {s}",
            f"Area = √[s(s-a)(s-b)(s-c)]",
            f"Area = √[{s} × {s-a} × {s-b} × {s-c}]",
            f"Area = {round_to_decimal(area, 4)}"
        ]
        
        return {
            'area': area,
            'semi_perimeter': s,
            'steps': steps,
            'formula': f'Area = {round_to_decimal(area, 4)} square units'
        }

    @staticmethod
    def rectangle_area(length: float, width: float) -> Dict[str, Any]:
        """Calculate area of a rectangle"""
        area = length * width
        perimeter = 2 * (length + width)
        
        steps = [
            f"Rectangle: Length = {length}, Width = {width}",
            f"Formula: Area = length × width",
            f"Area = {length} × {width} = {round_to_decimal(area, 4)}",
            f"Perimeter = 2(length + width) = 2({length} + {width}) = {round_to_decimal(perimeter, 4)}"
        ]
        
        return {
            'area': area,
            'perimeter': perimeter,
            'steps': steps,
            'formula': f'Area = {round_to_decimal(area, 4)}, Perimeter = {round_to_decimal(perimeter, 4)}'
        }

    @staticmethod
    def circle_area(radius: float) -> Dict[str, Any]:
        """Calculate area of a circle"""
        area = math.pi * radius**2
        circumference = 2 * math.pi * radius
        
        steps = [
            f"Circle with radius = {radius}",
            f"Formula: Area = πr²",
            f"Area = π × {radius}² = π × {radius**2} = {round_to_decimal(area, 4)}",
            f"Circumference = 2πr = 2 × π × {radius} = {round_to_decimal(circumference, 4)}"
        ]
        
        return {
            'area': area,
            'circumference': circumference,
            'steps': steps,
            'formula': f'Area = {round_to_decimal(area, 4)}, Circumference = {round_to_decimal(circumference, 4)}'
        }

    @staticmethod
    def circle_area_diameter(diameter: float) -> Dict[str, Any]:
        """Calculate area of a circle given diameter"""
        radius = diameter / 2
        return GeometryCalculator.circle_area(radius)

    @staticmethod
    def parallelogram_area(base: float, height: float) -> Dict[str, Any]:
        """Calculate area of a parallelogram"""
        area = base * height
        
        steps = [
            f"Parallelogram: Base = {base}, Height = {height}",
            f"Formula: Area = base × height",
            f"Area = {base} × {height} = {round_to_decimal(area, 4)}"
        ]
        
        return {
            'area': area,
            'steps': steps,
            'formula': f'Area = {round_to_decimal(area, 4)}'
        }

    @staticmethod
    def trapezoid_area(base1: float, base2: float, height: float) -> Dict[str, Any]:
        """Calculate area of a trapezoid"""
        area = ((base1 + base2) / 2) * height
        
        steps = [
            f"Trapezoid: Base1 = {base1}, Base2 = {base2}, Height = {height}",
            f"Formula: Area = [(b₁ + b₂) / 2] × h",
            f"Area = [({base1} + {base2}) / 2] × {height}",
            f"Area = {(base1 + base2) / 2} × {height} = {round_to_decimal(area, 4)}"
        ]
        
        return {
            'area': area,
            'steps': steps,
            'formula': f'Area = {round_to_decimal(area, 4)}'
        }

    @staticmethod
    def ellipse_area(semi_major: float, semi_minor: float) -> Dict[str, Any]:
        """Calculate area of an ellipse"""
        area = math.pi * semi_major * semi_minor
        
        steps = [
            f"Ellipse: Semi-major axis = {semi_major}, Semi-minor axis = {semi_minor}",
            f"Formula: Area = π × a × b",
            f"Area = π × {semi_major} × {semi_minor} = {round_to_decimal(area, 4)}"
        ]
        
        return {
            'area': area,
            'steps': steps,
            'formula': f'Area = {round_to_decimal(area, 4)}'
        }

    # ------ 3D Shapes ------

    @staticmethod
    def sphere_volume(radius: float) -> Dict[str, Any]:
        """Calculate volume of a sphere"""
        volume = (4/3) * math.pi * radius**3
        surface_area = 4 * math.pi * radius**2
        
        steps = [
            f"Sphere with radius = {radius}",
            f"Formula: Volume = (4/3)πr³",
            f"Volume = (4/3) × π × {radius}³",
            f"Volume = {round_to_decimal(volume, 4)}",
            f"Surface Area = 4πr² = {round_to_decimal(surface_area, 4)}"
        ]
        
        return {
            'volume': volume,
            'surface_area': surface_area,
            'steps': steps,
            'formula': f'Volume = {round_to_decimal(volume, 4)}, Surface Area = {round_to_decimal(surface_area, 4)}'
        }

    @staticmethod
    def cube_volume(side: float) -> Dict[str, Any]:
        """Calculate volume and surface area of a cube"""
        volume = side**3
        surface_area = 6 * side**2
        
        steps = [
            f"Cube with side = {side}",
            f"Formula: Volume = s³",
            f"Volume = {side}³ = {round_to_decimal(volume, 4)}",
            f"Surface Area = 6s² = 6 × {side}² = {round_to_decimal(surface_area, 4)}"
        ]
        
        return {
            'volume': volume,
            'surface_area': surface_area,
            'steps': steps,
            'formula': f'Volume = {round_to_decimal(volume, 4)}, Surface Area = {round_to_decimal(surface_area, 4)}'
        }

    @staticmethod
    def rectangular_prism_volume(length: float, width: float, height: float) -> Dict[str, Any]:
        """Calculate volume of a rectangular prism"""
        volume = length * width * height
        surface_area = 2 * (length*width + length*height + width*height)
        
        steps = [
            f"Rectangular Prism: L={length}, W={width}, H={height}",
            f"Formula: Volume = l × w × h",
            f"Volume = {length} × {width} × {height} = {round_to_decimal(volume, 4)}",
            f"Surface Area = 2(lw + lh + wh) = {round_to_decimal(surface_area, 4)}"
        ]
        
        return {
            'volume': volume,
            'surface_area': surface_area,
            'steps': steps,
            'formula': f'Volume = {round_to_decimal(volume, 4)}, Surface Area = {round_to_decimal(surface_area, 4)}'
        }

    @staticmethod
    def cylinder_volume(radius: float, height: float) -> Dict[str, Any]:
        """Calculate volume of a cylinder"""
        volume = math.pi * radius**2 * height
        lateral_area = 2 * math.pi * radius * height
        total_surface = lateral_area + 2 * math.pi * radius**2
        
        steps = [
            f"Cylinder: Radius = {radius}, Height = {height}",
            f"Formula: Volume = πr²h",
            f"Volume = π × {radius}² × {height} = {round_to_decimal(volume, 4)}",
            f"Lateral Surface Area = 2πrh = {round_to_decimal(lateral_area, 4)}",
            f"Total Surface Area = {round_to_decimal(total_surface, 4)}"
        ]
        
        return {
            'volume': volume,
            'lateral_area': lateral_area,
            'total_surface': total_surface,
            'steps': steps,
            'formula': f'Volume = {round_to_decimal(volume, 4)}'
        }

    @staticmethod
    def cone_volume(radius: float, height: float) -> Dict[str, Any]:
        """Calculate volume of a cone"""
        volume = (1/3) * math.pi * radius**2 * height
        slant_height = math.sqrt(radius**2 + height**2)
        lateral_area = math.pi * radius * slant_height
        
        steps = [
            f"Cone: Radius = {radius}, Height = {height}",
            f"Formula: Volume = (1/3)πr²h",
            f"Volume = (1/3) × π × {radius}² × {height} = {round_to_decimal(volume, 4)}",
            f"Slant Height = √(r² + h²) = {round_to_decimal(slant_height, 4)}",
            f"Lateral Surface Area = πrl = {round_to_decimal(lateral_area, 4)}"
        ]
        
        return {
            'volume': volume,
            'slant_height': slant_height,
            'lateral_area': lateral_area,
            'steps': steps,
            'formula': f'Volume = {round_to_decimal(volume, 4)}'
        }

    @staticmethod
    def pyramid_volume(base_area: float, height: float) -> Dict[str, Any]:
        """Calculate volume of a pyramid"""
        volume = (1/3) * base_area * height
        
        steps = [
            f"Pyramid: Base Area = {base_area}, Height = {height}",
            f"Formula: Volume = (1/3) × Base Area × Height",
            f"Volume = (1/3) × {base_area} × {height} = {round_to_decimal(volume, 4)}"
        ]
        
        return {
            'volume': volume,
            'steps': steps,
            'formula': f'Volume = {round_to_decimal(volume, 4)}'
        }

    # ------ Angles & Trigonometry ------

    @staticmethod
    def pythagorean_theorem(a: float, b: float) -> Dict[str, Any]:
        """Calculate hypotenuse using Pythagorean theorem"""
        c = math.sqrt(a**2 + b**2)
        
        steps = [
            f"Right Triangle: a = {a}, b = {b}",
            f"Formula: c² = a² + b²",
            f"c² = {a}² + {b}² = {a**2} + {b**2} = {a**2 + b**2}",
            f"c = √{a**2 + b**2} = {round_to_decimal(c, 4)}"
        ]
        
        return {
            'hypotenuse': c,
            'steps': steps,
            'formula': f'c = {round_to_decimal(c, 4)}'
        }

    @staticmethod
    def polygon_area(sides: int, side_length: float) -> Dict[str, Any]:
        """Calculate area of a regular polygon"""
        area = (sides * side_length**2) / (4 * math.tan(math.pi / sides))
        
        steps = [
            f"Regular Polygon: {sides} sides, Side length = {side_length}",
            f"Formula: Area = (n × s²) / (4 × tan(π/n))",
            f"Area = {round_to_decimal(area, 4)}"
        ]
        
        return {
            'area': area,
            'steps': steps,
            'formula': f'Area = {round_to_decimal(area, 4)}'
        }

    @staticmethod
    def distance_3d(x1: float, y1: float, z1: float, 
                   x2: float, y2: float, z2: float) -> Dict[str, Any]:
        """Calculate distance between two points in 3D"""
        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
        
        steps = [
            f"Points: ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2})",
            f"Formula: d = √[(x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²]",
            f"d = √[{(x2-x1)**2} + {(y2-y1)**2} + {(z2-z1)**2}]",
            f"Distance = {round_to_decimal(distance, 4)}"
        ]
        
        return {
            'distance': distance,
            'steps': steps,
            'formula': f'Distance = {round_to_decimal(distance, 4)}'
        }


# Public functions
def triangle_area(base, height):
    """Calculate triangle area"""
    return GeometryCalculator.triangle_area(base, height)['area']


def circle_area(radius):
    """Calculate circle area"""
    return GeometryCalculator.circle_area(radius)['area']


def sphere_volume(radius):
    """Calculate sphere volume"""
    return GeometryCalculator.sphere_volume(radius)['volume']


def cube_volume(side):
    """Calculate cube volume"""
    return GeometryCalculator.cube_volume(side)['volume']
