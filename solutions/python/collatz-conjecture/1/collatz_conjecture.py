def steps(number):
    """
    return the number of steps it takes to reach 1 according to the
    rules of the Collatz Conjecture
    """
    step_counter = 0
    
    if number < 1:
        raise ValueError('Only positive integers are allowed')
    
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number * 3 + 1
        step_counter += 1

    return step_counter