def eliminateFromOnetoOne(lista,listb):
    '''
    This function eliminates all words in one list from another list.
    '''
    for items in listb:
        while lista.count(items) > 0:
            lista.reomve(items)
    return lista
