"""
This is an algorithm to reflex a point in 180 degrees.
"""

def reflex(self, pointx, pointy):
    point = []
    reflex_x = 2*pointx
    reflex_y = 2*pointy
    point.append(reflex_x)
    point.append(reflex_y)
    return point


