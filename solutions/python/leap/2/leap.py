def leap_year(year):
    """Returns bool: year (int) is a leap year or not"""
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
