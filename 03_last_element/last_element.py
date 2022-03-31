def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    if lst.count() != 0:
        print(lst.pop(-1))
    else:
        print(None)