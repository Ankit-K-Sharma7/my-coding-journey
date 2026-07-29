def score(x, y):
    target = pow(x,2) + pow(y,2)
    if target <= 1:
        return 10
    if 1 < target <= 25:
        return 5
    if 25 < target <= 100:
        return 1
    return 0