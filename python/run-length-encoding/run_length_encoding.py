def decode(string):
    result = []
    num = 0

    for char in string:
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            count = num if num else 1
            result.append(count * char)
            num = 0

    return "".join(result)

def encode(string):
    if not string:
        return ""

    result = []
    count = 1

    for char in range(len(string) - 1):
        if string[char] == string[char + 1]:
            count += 1
        else:
            result.append((str(count) if count > 1 else "") + string[char])
            count = 1

    result.append((str(count) if count > 1 else "") + string[-1])

    return "".join(result)