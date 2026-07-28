def rotate(text, key):
    cipher = []
    for letter in text:
        if letter.isupper():
            cipher.append(chr((ord(letter) - ord("A") + key) % 26 + ord("A")))
        elif letter.islower():
            cipher.append(chr((ord(letter) - ord("a") + key) % 26 + ord("a")))
        else:
            cipher.append(letter)
    return "".join(cipher)
