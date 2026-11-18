COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def label(colors):
    value = (10 * COLORS.index(colors[0]) + COLORS.index(colors[1])) * 10 ** COLORS.index(colors[2])

    if value == 0:
        return "0 ohms"
    
    label = ""
    prefix = {"giga": 10 ** 9, "mega": 10 ** 6, "kilo": 10 ** 3, "": 1}
    for unit, divisor in prefix.items():
        if value >= divisor:
            label = f"{value/divisor:g} {unit}"
            break
    
    return label + "ohms"