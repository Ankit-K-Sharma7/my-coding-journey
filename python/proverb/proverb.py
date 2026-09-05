def proverb(*words, qualifier=None):
    result = []

    for index in range(len(words) - 1):
        result.append(f"For want of a {words[index]} the {words[index + 1]} was lost.")
    if words:
        if qualifier:
            result.append(f"And all for the want of a {qualifier} {words[0]}.")
        else:
            result.append(f"And all for the want of a {words[0]}.")
    return result