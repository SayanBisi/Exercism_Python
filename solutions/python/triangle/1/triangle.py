def equilateral(sides):
    """
    Checks if all sides of a triangle are of the same length
    """
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """
    Checks if at least any 2 sides of a triangle are of the same length
    """
    if not is_valid_triangle(sides):
        return False
    side1, side2, side3 = sorted(sides)
    return (equilateral(sides) or side1 == side2
           or side2 == side3)

def scalene(sides):
    """
    Checks if all sides of a triangle are of different length
    """
    if not is_valid_triangle(sides):
        return False
    return not equilateral(sides) and not isosceles(sides)

def degenerate(sides):
    """
    Checks if sum of 2 sides of a triangle equals the third side
    """
    if not is_valid_triangle(sides):
        return False
    side1, side2, side3 = sorted(sides)
    return side1 + side2 == side3

def is_valid_triangle(sides):
    """
    Checks if the given set of lengths results in a valid triangle
    """
    validity = True
    if len(sides) != 3 or any(side <= 0 for side in sides):
        validity = False
    else:
        side1, side2, side3 = sorted(sides)
        if side1 + side2 < side3:
            validity = False

    return validity