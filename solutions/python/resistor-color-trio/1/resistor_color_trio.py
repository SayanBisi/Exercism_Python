COLORS = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

def label(colors):
    a, b, c = (COLORS[color] for color in colors[:3])
    value = (10 * a + b) * 10 ** c

    for divisor, unit in (
        (10**9, "gigaohms"),
        (10**6, "megaohms"),
        (10**3, "kiloohms")
    ):
        if value >= divisor:
            return f"{value / divisor:g} {unit}"

    return f"{value} ohms"
