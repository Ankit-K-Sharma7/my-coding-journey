def color_code(color):
    color_list = colors()
    code_list = list(range(10))
    color_map = dict(zip(color_list , code_list))
    return color_map[color]


def colors():
    color = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]
    return color
