def color_code(color):
    '''
    Returns the number associated with a color
    params: color (str) - the color whose numerical value is to be found
    returns: int - the numerical value of the color
    '''
    resistor_colors = colors()
    return resistor_colors.index(color)


def colors():
    '''
    Returns a list of all possible band colors
    returns: list - all possible resistor band colors
    '''
    return ['black',
           'brown',
           'red',
           'orange',
           'yellow',
           'green',
           'blue',
           'violet',
           'grey',
            'white']
