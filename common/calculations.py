from math import sqrt


def calculate_distance(x1, y1, x2, y2):
    distance = sqrt(abs((x2 - x1) ** 2 + (y2 - y1) ** 2))  # distance in [ m ]
    return distance
