def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_str = ""
    for char in range (len(phrase)):
        if phrase[char].isupper():
            new_str+=phrase[char].lower()
        elif phrase[char].islower():
            new_str+=phrase[char].upper() 
    return(new_str)  