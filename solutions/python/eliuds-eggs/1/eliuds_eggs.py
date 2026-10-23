def egg_count(display_value):
    count_ones = 0
    num = display_value
    while num != 0:
        if num % 2 != 0:
            count_ones += 1
        num //= 2

    return count_ones