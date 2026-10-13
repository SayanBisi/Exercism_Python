
def square(number):   
    """
    Calculates number of grains on a given square of the chessboard
    Params:
    number (int): The index number of the square on the chessboard
    Returns:
    int: The number of grains on the square of the given number
    """
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    
    return pow(2, number - 1)

def total():
    """
    Calculates total number of grains on all squares of the chessboard
    Returns:
    int: The total number of grains on the entire chessboard
    """
    total_grains = 0
    
    for num in range(1, 65):
        total_grains += square(num)
    
    return total_grains