def isTriangle(sides):
    a,b,c = sides[::1]
    if (a + b >= c) and (b + c >= a) and (a + c >= b) and (sides[::1] > [0,0,0] ) is True:
        result = True
    else:
        result = False
    return result

def equilateral(sides):
    a,b,c = sides[::1]
    condition = isTriangle(sides)
    if (a == b == c) and condition is True:
        triangle = True
    else:
        triangle = False
    return triangle


def isosceles(sides):
    a,b,c = sides[::1]
    condition = isTriangle(sides)
    if (a == b or b == c or a == c ) and condition is True:
        triangle = True
    else:
        triangle = False
    return triangle


def scalene(sides):
    a,b,c = sides[::1]
    condition = isTriangle(sides)
    if (a != b != c != a) and condition is True:
        triangle = True
    else:
        triangle = False
    return triangle
    
