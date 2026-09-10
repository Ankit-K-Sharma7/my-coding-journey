def rows(letter):
    n = ord(letter) - ord("A")
    result = []

    for i in range(n + 1):
        outer = n - i
        inner = 2 * i - 1

        if i == 0:
            result.append(" " * outer + "A" + " " * outer)
        else:
            result.append(" " * outer + chr(ord("A") + i) +" " * inner + chr(ord("A") + i) +" " * outer)

    return result + result[-2::-1]