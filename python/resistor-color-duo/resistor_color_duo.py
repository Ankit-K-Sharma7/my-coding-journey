def value(colors):
    code = 0
    color_map = {"black":0,"brown":1,"red":2,"orange":3,"yellow":4,"green":5,"blue":6,"violet":7,"grey":8,"white":9}
    for color in colors[:2]:
        code = color_map[color] + 10 * code
    return code