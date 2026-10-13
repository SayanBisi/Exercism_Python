def is_armstrong_number(number):
    """
    Checks if the given number argument is an Armstrong number.
    """
    num_copy = number
    digits = []
    while num_copy > 0:
        digits.append(num_copy % 10)
        num_copy //= 10
    num_digits = len(digits)
    armstrong_sum = sum(digit ** num_digits for digit in digits)
    return number == armstrong_sum