"""
Statistics Module - Mean, median, mode, standard deviation, variance, and statistical analysis
"""

import math
from typing import Dict, Any, List, Union
from ..utils.helpers import round_to_decimal


class StatisticsCalculator:
    """Calculates statistical measures with step-by-step explanations"""

    @staticmethod
    def mean(data: List[Union[int, float]]) -> Dict[str, Any]:
        """Calculate arithmetic mean (average)"""
        if len(data) == 0:
            raise ValueError("Cannot calculate mean of empty dataset")
        
        total = sum(data)
        mean_value = total / len(data)
        
        steps = [
            f"Data: {data}",
            f"Sum: {' + '.join(str(x) for x in data)} = {total}",
            f"Count: {len(data)}",
            f"Mean = Sum / Count = {total} / {len(data)} = {round_to_decimal(mean_value, 4)}"
        ]
        
        return {
            'mean': mean_value,
            'steps': steps,
            'formula': f'Mean = {round_to_decimal(mean_value, 4)}'
        }

    @staticmethod
    def median(data: List[Union[int, float]]) -> Dict[str, Any]:
        """Calculate median (middle value)"""
        if len(data) == 0:
            raise ValueError("Cannot calculate median of empty dataset")
        
        sorted_data = sorted(data)
        n = len(sorted_data)
        
        if n % 2 == 1:
            # Odd number of elements
            median_value = sorted_data[n // 2]
            steps = [
                f"Data: {data}",
                f"Sorted: {sorted_data}",
                f"Number of elements: {n} (odd)",
                f"Median is the middle element: {median_value}"
            ]
        else:
            # Even number of elements
            middle1 = sorted_data[n // 2 - 1]
            middle2 = sorted_data[n // 2]
            median_value = (middle1 + middle2) / 2
            steps = [
                f"Data: {data}",
                f"Sorted: {sorted_data}",
                f"Number of elements: {n} (even)",
                f"Median = ({middle1} + {middle2}) / 2 = {median_value}"
            ]
        
        return {
            'median': median_value,
            'steps': steps,
            'formula': f'Median = {round_to_decimal(median_value, 4)}'
        }

    @staticmethod
    def mode(data: List[Union[int, float]]) -> Dict[str, Any]:
        """Calculate mode (most frequent value)"""
        if len(data) == 0:
            raise ValueError("Cannot calculate mode of empty dataset")
        
        frequency = {}
        for value in data:
            frequency[value] = frequency.get(value, 0) + 1
        
        max_freq = max(frequency.values())
        modes = [value for value, freq in frequency.items() if freq == max_freq]
        
        steps = [
            f"Data: {data}",
            f"Frequency: {frequency}",
            f"Mode(s): {modes} (appears {max_freq} times)"
        ]
        
        return {
            'mode': modes[0] if len(modes) == 1 else modes,
            'frequency': frequency,
            'steps': steps,
            'formula': f"Mode = {modes[0] if len(modes) == 1 else modes}"
        }

    @staticmethod
    def range(data: List[Union[int, float]]) -> Dict[str, Any]:
        """Calculate range (max - min)"""
        if len(data) == 0:
            raise ValueError("Cannot calculate range of empty dataset")
        
        min_value = min(data)
        max_value = max(data)
        range_value = max_value - min_value
        
        steps = [
            f"Data: {data}",
            f"Maximum: {max_value}",
            f"Minimum: {min_value}",
            f"Range = Max - Min = {max_value} - {min_value} = {range_value}"
        ]
        
        return {
            'range': range_value,
            'min': min_value,
            'max': max_value,
            'steps': steps,
            'formula': f'Range = {range_value}'
        }

    @staticmethod
    def variance(data: List[Union[int, float]], sample: bool = False) -> Dict[str, Any]:
        """
        Calculate variance
        sample = False for population variance
        sample = True for sample variance
        """
        if len(data) == 0:
            raise ValueError("Cannot calculate variance of empty dataset")
        
        mean_value = sum(data) / len(data)
        
        squared_diffs = [(x - mean_value)**2 for x in data]
        sum_squared_diffs = sum(squared_diffs)
        
        if sample and len(data) > 1:
            variance_value = sum_squared_diffs / (len(data) - 1)
            divisor = len(data) - 1
            var_type = "Sample"
        else:
            variance_value = sum_squared_diffs / len(data)
            divisor = len(data)
            var_type = "Population"
        
        steps = [
            f"Data: {data}",
            f"Mean: {round_to_decimal(mean_value, 4)}",
            f"Squared differences from mean: {[round_to_decimal(x, 4) for x in squared_diffs]}",
            f"Sum of squared differences: {round_to_decimal(sum_squared_diffs, 4)}",
            f"{var_type} Variance = Sum / {divisor} = {round_to_decimal(variance_value, 4)}"
        ]
        
        return {
            'variance': variance_value,
            'type': var_type,
            'steps': steps,
            'formula': f'Variance = {round_to_decimal(variance_value, 4)}'
        }

    @staticmethod
    def standard_deviation(data: List[Union[int, float]], sample: bool = False) -> Dict[str, Any]:
        """
        Calculate standard deviation
        sample = False for population std dev
        sample = True for sample std dev
        """
        variance_result = StatisticsCalculator.variance(data, sample)
        variance_value = variance_result['variance']
        std_dev = math.sqrt(variance_value)
        
        steps = variance_result['steps'] + [
            f"Standard Deviation = √Variance = √{round_to_decimal(variance_value, 4)} = {round_to_decimal(std_dev, 4)}"
        ]
        
        return {
            'std_dev': std_dev,
            'variance': variance_value,
            'steps': steps,
            'formula': f'Std Dev = {round_to_decimal(std_dev, 4)}'
        }

    @staticmethod
    def quartiles(data: List[Union[int, float]]) -> Dict[str, Any]:
        """Calculate quartiles (Q1, Q2, Q3)"""
        if len(data) < 4:
            raise ValueError("Need at least 4 data points for quartiles")
        
        sorted_data = sorted(data)
        
        # Q2 is the median
        q2 = StatisticsCalculator.median(sorted_data)['median']
        
        # Split data and find Q1 and Q3
        mid = len(sorted_data) // 2
        if len(sorted_data) % 2 == 0:
            lower_half = sorted_data[:mid]
            upper_half = sorted_data[mid:]
        else:
            lower_half = sorted_data[:mid]
            upper_half = sorted_data[mid+1:]
        
        q1 = StatisticsCalculator.median(lower_half)['median']
        q3 = StatisticsCalculator.median(upper_half)['median']
        iqr = q3 - q1
        
        steps = [
            f"Data: {data}",
            f"Sorted: {sorted_data}",
            f"Q1 (1st Quartile): {round_to_decimal(q1, 4)} (25th percentile)",
            f"Q2 (Median): {round_to_decimal(q2, 4)} (50th percentile)",
            f"Q3 (3rd Quartile): {round_to_decimal(q3, 4)} (75th percentile)",
            f"IQR (Q3 - Q1): {round_to_decimal(iqr, 4)}"
        ]
        
        return {
            'Q1': q1,
            'Q2': q2,
            'Q3': q3,
            'IQR': iqr,
            'steps': steps,
            'formula': f'Q1={round_to_decimal(q1, 4)}, Q2={round_to_decimal(q2, 4)}, Q3={round_to_decimal(q3, 4)}'
        }

    @staticmethod
    def z_score(value: float, mean: float, std_dev: float) -> Dict[str, Any]:
        """Calculate z-score (standardized score)"""
        if std_dev == 0:
            raise ValueError("Standard deviation cannot be zero")
        
        z = (value - mean) / std_dev
        
        steps = [
            f"Value: {value}",
            f"Mean: {mean}",
            f"Standard Deviation: {std_dev}",
            f"Formula: z = (value - mean) / std_dev",
            f"z = ({value} - {mean}) / {std_dev}",
            f"z = {value - mean} / {std_dev}",
            f"z-score = {round_to_decimal(z, 4)}"
        ]
        
        return {
            'z_score': z,
            'steps': steps,
            'formula': f'z-score = {round_to_decimal(z, 4)}'
        }

    @staticmethod
    def correlation_coefficient(x_data: List[float], y_data: List[float]) -> Dict[str, Any]:
        """Calculate Pearson correlation coefficient"""
        if len(x_data) != len(y_data):
            raise ValueError("x and y data must have same length")
        
        if len(x_data) < 2:
            raise ValueError("Need at least 2 data points")
        
        n = len(x_data)
        x_mean = sum(x_data) / n
        y_mean = sum(y_data) / n
        
        numerator = sum((x_data[i] - x_mean) * (y_data[i] - y_mean) for i in range(n))
        x_variance = sum((x - x_mean)**2 for x in x_data)
        y_variance = sum((y - y_mean)**2 for y in y_data)
        denominator = math.sqrt(x_variance * y_variance)
        
        if denominator == 0:
            correlation = 0
        else:
            correlation = numerator / denominator
        
        steps = [
            f"X data: {x_data}",
            f"Y data: {y_data}",
            f"X mean: {round_to_decimal(x_mean, 4)}",
            f"Y mean: {round_to_decimal(y_mean, 4)}",
            f"Pearson's r = {round_to_decimal(correlation, 4)}",
            f"Interpretation: ", 
            f"  r = 1: Perfect positive correlation",
            f"  r = 0: No correlation",
            f"  r = -1: Perfect negative correlation"
        ]
        
        return {
            'correlation': correlation,
            'steps': steps,
            'formula': f'r = {round_to_decimal(correlation, 4)}'
        }

    @staticmethod
    def linear_regression(x_data: List[float], y_data: List[float]) -> Dict[str, Any]:
        """Calculate linear regression line y = mx + b"""
        if len(x_data) != len(y_data):
            raise ValueError("x and y data must have same length")
        
        n = len(x_data)
        x_mean = sum(x_data) / n
        y_mean = sum(y_data) / n
        
        numerator = sum((x_data[i] - x_mean) * (y_data[i] - y_mean) for i in range(n))
        denominator = sum((x - x_mean)**2 for x in x_data)
        
        m = numerator / denominator  # slope
        b = y_mean - m * x_mean  # y-intercept
        
        steps = [
            f"X data: {x_data}",
            f"Y data: {y_data}",
            f"X mean: {round_to_decimal(x_mean, 4)}",
            f"Y mean: {round_to_decimal(y_mean, 4)}",
            f"Slope (m) = {round_to_decimal(m, 4)}",
            f"Y-intercept (b) = {round_to_decimal(b, 4)}",
            f"Linear regression equation: y = {round_to_decimal(m, 4)}x + {round_to_decimal(b, 4)}"
        ]
        
        return {
            'slope': m,
            'intercept': b,
            'equation': f'y = {round_to_decimal(m, 4)}x + {round_to_decimal(b, 4)}',
            'steps': steps,
            'formula': f'y = {round_to_decimal(m, 4)}x + {round_to_decimal(b, 4)}'
        }


# Public functions
def mean(data):
    """Calculate mean"""
    return StatisticsCalculator.mean(data)['mean']


def median(data):
    """Calculate median"""
    return StatisticsCalculator.median(data)['median']


def mode(data):
    """Calculate mode"""
    return StatisticsCalculator.mode(data)['mode']


def std_dev(data, sample=False):
    """Calculate standard deviation"""
    return StatisticsCalculator.standard_deviation(data, sample)['std_dev']
