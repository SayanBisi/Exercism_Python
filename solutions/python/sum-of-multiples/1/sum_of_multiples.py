def sum_of_multiples(limit, multiples):
    numbers = set()
    for factor in multiples:
        if factor == 0:
            continue
        numbers |= set(range(factor, limit, factor))

    return sum(numbers)