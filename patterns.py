import random

def random_pattern(columns, rows, density=0.2):
    return {(c, r): 0 for c in range(columns) for r in range(rows) if random.random() < density}

def blinker_pattern():
    return {(10, 10): 0, (11, 10): 0, (12, 10): 0}

def glider_pattern():
    return {(10, 10): 0, (11, 10): 0, (12, 10): 0, (12, 9): 0, (11, 8): 0}
