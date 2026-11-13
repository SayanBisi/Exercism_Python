def score(x, y):
    dart_landing = 0
    radius_squared = x * x + y * y
    if 0 <= radius_squared <= 1:
        dart_landing = 10
    elif 1 < radius_squared <= 25:
        dart_landing = 5
    elif 25 < radius_squared <= 100:
        dart_landing = 1
    else:
        dart_landing = 0

    return dart_landing