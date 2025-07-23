# CONST VALUES
HEAVY = 20
BULKY_AREA = 1000000
BULKY_DIMENSION = 150

def isHeavy(mass):
    """ Determines if a package is considered heavy.

    Args:
        mass (int): The mass of the package in kg.
        
    Throws:
        Exception: When weight <= 0.

    Returns:
        bool: True if the package is heavy, false otherwise.
    """
    if mass <= 0:
        raise Exception("Mass cannot be non-possitive number.")
    
    return mass > 20


def isBulky(w, h, l):
    """ Determines if a package is considered bulky.

    Args:
        w (int): the width of the package in cm.
        h (int): The height of the package in cm.
        l (int): The length of the package in cm.
        
    Throws:
        Exception: When any of the inputs are <= 0.

    Returns:
        bool: True if any are true -> w, h, or l >= 150cm OR w*h*l >= 1m cm^3.
    """
    if w <= 0 or h <= 0 or l <= 0:
        raise Exception("One or more dimension is invalid.")
    
    dimensions = [w, h, l]
    for dimension in dimensions:
        if dimension >= BULKY_DIMENSION:
            return True
        
    return w * h * l >= BULKY_AREA


def sort(width, height, length, mass):
    """ Determines if a package is STANDARD, SPECIAL, or REJECTED shipping type.

    Args:
        width (int): The width of the package in cm.
        height (int): The height of the package in cm.
        length (int): The length of the package in cm.
        mass (int): The mass of the package in kg.

    Throws:
        Exception: When any of the inputs are <= 0.

    Returns:
        string: The name of the stack the package should go to.
    """
    
    heavy = isHeavy(mass)
    bulky = isBulky(width, height, length)

    if heavy and bulky:
        return 'REJECTED'

    if heavy or bulky:
        return 'SPECIAL'
    return 'STANDARD'
