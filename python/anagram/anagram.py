def find_anagrams(word, candidates):
    anagram_words = []
    for words in candidates:
        if (sorted(word.lower()) == sorted(words.lower()) and word.lower() != words.lower()):
            anagram_words.append(words)
    return anagram_words
