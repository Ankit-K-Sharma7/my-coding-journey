def convert(number):
    """
    Return the sound of raindrops.
    
    Parameters:
        number (int): The number of raindrops.
        
    Returns:
       ("Pling", "Plang", "Plong" (str): The sound of raindrops.

    Your task is to convert a number into its corresponding raindrop sounds.

    If a given number:
    is divisible by 3, add "Pling" to the result.
    is divisible by 5, add "Plang" to the result.
    is divisible by 7, add "Plong" to the result.
    is not divisible by 3, 5, or 7, the result should be the number as a string.
    """
    raindrop_sound = ""
    if number % 3 == 0:
        raindrop_sound += "Pling"
    if number % 5 == 0:
        raindrop_sound += "Plang"
    if number % 7 == 0:
        raindrop_sound += "Plong"
    return str(number) if not raindrop_sound else raindrop_sound
