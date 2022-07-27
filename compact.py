def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    lst_copy = []
    for i in lst:
        if(bool(i) == True):
            lst_copy.append(i)
    return lst_copy