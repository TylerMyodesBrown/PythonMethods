def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for l in lst:
        if isinstance(l, list):
            print(True)
            return True
        else:
            print(False)
            return(False)

    