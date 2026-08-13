import string
def is_pangram(sentence):
    sentence = set(sentence.lower())

    if len(sentence & set(string.ascii_lowercase)) < 26:
        return False
    return True