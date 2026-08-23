def is_isogram(phrase):
    phrase = phrase.lower().replace("-" , "").replace(" ","")
    return len(phrase) == len(set(phrase))