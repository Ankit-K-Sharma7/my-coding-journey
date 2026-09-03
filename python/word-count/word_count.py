import string

def count_words(sentence):
    sentence = sentence.lower()
    word_count = {}
    for char in string.punctuation:
        if char != "'":
            sentence = sentence.replace(char," ")
    words = sentence.split()
    for word in words:
        word = word.strip("'")
        if word :
            word_count[word] = word_count.setdefault(word ,0) + 1
    return word_count