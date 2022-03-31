def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """


    thing = {}

    for l in phrase:
        thing[l] = thing.get(l, 0)+1

    print(thing)
    return thing


multiple_letter_count('yay')
multiple_letter_count('Yay')