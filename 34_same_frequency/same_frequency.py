def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    n1 = [int(num) for num in str(num1)]
    n2 = [int(num) for num in str(num2)]

    n1.sort()
    n2.sort()

    if n1 == n2:
        print(True)
        return True
    else:
        print(False)
        return False