"""
https://btechgeeks.com/python-program-for-arc-length-from-given-angle/
"""
#we will do the formula of arc length finding
# 2 * pi * radius (angle/ 360)
#to get preceise pi value we will use math module
from math import pi

def arc_length(angle, radius):
    if not isinstance(angle, int) or (not isinstance(radius, int) or isinstance(radius, float)):
        raise ValueError('Got an Inappropriate Values')
    return 2 * pi * radius * ( angle / 360 )

print(arc_length(90, 10))
