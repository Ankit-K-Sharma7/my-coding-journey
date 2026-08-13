def is_valid(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False

    total = 0

    for index in range(10):
        if isbn[index] == "X" and index == 9:
            digit = 10
        elif isbn[index].isdigit():
            digit = int(isbn[index])
        else:
            return False

        total += digit * (10 - index)
    return total % 11 == 0