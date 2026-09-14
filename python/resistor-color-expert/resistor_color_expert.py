def resistor_label(colors):
    values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    tolerance = {
        "grey": 0.05,
        "violet": 0.1,
        "blue": 0.25,
        "green": 0.5,
        "brown": 1,
        "red": 2,
        "gold": 5,
        "silver": 10
    }

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        number = values[colors[0]] * 10 + values[colors[1]]
        multiplier = values[colors[2]]
        tol = tolerance[colors[3]]

    else:
        number = (
            values[colors[0]] * 100
            + values[colors[1]] * 10
            + values[colors[2]]
        )
        multiplier = values[colors[3]]
        tol = tolerance[colors[4]]

    resistance = number * (10 ** multiplier)

    if resistance >= 1_000_000:
        resistance /= 1_000_000
        unit = "megaohms"
    elif resistance >= 1_000:
        resistance /= 1_000
        unit = "kiloohms"
    else:
        unit = "ohms"

    return f"{resistance:g} {unit} ±{tol:g}%"