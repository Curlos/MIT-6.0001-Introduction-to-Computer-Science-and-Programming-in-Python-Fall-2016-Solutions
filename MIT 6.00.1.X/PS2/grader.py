import math


def area(n, s):
    '''Calculates the area of a polygon.'''
    return (0.25 * n * (s**2)) / (math.tan(math.pi / n))


def perimeter(n, s):
    '''Calculates the perimeter of a polygon.'''
    return n * s


def polysum(n, s):
    '''Sums the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.'''
    return round(area(n, s) + (perimeter(n, s) ** 2), 4)



