import random

def random_pattern(columns, rows, density=0.2):
    return {(c, r) for c in range(columns) for r in range(rows) if random.random() < density}

def blinker_pattern():
    return [(10, 10), (11, 10), (12, 10)]

def glider_pattern():
    return [(10, 10), (11, 10), (12, 10), (12, 9), (11, 8)]
