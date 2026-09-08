def recite(start, take=1):
    verse_map = {10 : "Ten" , 9 : "Nine" , 8 : "Eight" , 7 : "Seven" , 6 : "Six" , 5 : "Five" , 4 : "Four" , 3 : "Three" , 2 : "Two" , 1 : "One" , 0 : "no"}
    verses = []
    current = start
    for index in range(take):
        current_bottle = "bottle" if current == 1 else "bottles"
        next_bottle = "bottle" if current == 2 else "bottles"

        verses.append(f"{verse_map[current]} green {current_bottle} hanging on the wall,")
        verses.append(f"{verse_map[current]} green {current_bottle} hanging on the wall,")
        verses.append("And if one green bottle should accidentally fall,")
        verses.append(f"There'll be {verse_map[current - 1].lower()} green {next_bottle} hanging on the wall.")
        
        if index < take - 1:
            verses.append("")
        current -= 1
    return verses
