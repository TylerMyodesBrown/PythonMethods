def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    print(lst.count(search_term))
    return lst.count(search_term)

frequency([1,2,2,3,3,4,1,2,3,123,1,23,1,2,3,1,], 2)