def append(elem, target):
    ''''Append an element to a list.'''
    target.append(elem)


def searchsorted(insert, target):
    '''Find the indices for elements in insert if they were to be inserted into the sorted list `target`.
    Assume both insert and target are sorted.
    '''
    result = []
    for i, compared in enumerate(target):
        for elem in insert[len(result):]:
            if elem <= compared:
                append(i, result)
    result += (len(insert) - len(result)) * [len(target)]
    return result


def insert_sorted(elems, target):
    '''Insert list `elems` into sorted list `target`.'''
    elems = list(sorted(elems))
    result = list(target)
    indices = searchsorted(elems, target)
    for index, elem in zip(indices[::-1], elems[::-1]):
        result.insert(index, elem)
    return result
