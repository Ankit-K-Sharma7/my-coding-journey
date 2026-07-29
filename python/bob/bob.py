def response(hey_bob):
    """ Bob only ever answers one of five things:
"Sure." This is his response if you ask him a question, such as "How are you?" The convention used for questions is that it ends with a question mark.
"Whoa, chill out!" This is his answer if you YELL AT HIM. The convention used for yelling is ALL CAPITAL LETTERS.
"Calm down, I know what I'm doing!" This is what he says if you yell a question at him.
"Fine. Be that way!" This is how he responds to silence. The convention used for silence is nothing, or various combinations of whitespace characters.
"Whatever." This is what he answers to anything else.
"""
    hey_bob = hey_bob.strip()

    if hey_bob == "":
        reply = "Fine. Be that way!"
    elif hey_bob.isupper() and not hey_bob.endswith("?"):
        reply = "Whoa, chill out!"
    elif hey_bob.isupper() and hey_bob.endswith("?"):
        reply = "Calm down, I know what I'm doing!"
    elif hey_bob.endswith("?"):
        reply = "Sure."
    else:
        reply = "Whatever."
    return reply
