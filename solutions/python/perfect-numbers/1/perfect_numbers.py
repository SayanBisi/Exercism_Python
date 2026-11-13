def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors_list = []
    classification = ''
    for factor in range(1, number):
        if number % factor == 0:
            factors_list.append(factor)
    sum_of_factors = sum(factors_list)
    if sum_of_factors == number:
        classification = 'perfect'
    elif sum_of_factors < number:
        classification = 'deficient'
    else:
        classification = 'abundant'
    return classification