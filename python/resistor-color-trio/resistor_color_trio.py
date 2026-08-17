def label(colors):
    color_map = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}

    code = color_map[colors[0]] * 10 + color_map[colors[1]]
    multiplier = 10 ** color_map[colors[2]]

    resistance = code * multiplier

    if resistance >= 1_000_000_000:
        return f"{resistance//1_000_000_000} gigaohms"
    if resistance >= 1_000_000:
        return f"{resistance//1_000_000} megaohms"
    if resistance >= 1000:
        return f"{resistance//1000} kiloohms"
    
    return f"{resistance} ohms"