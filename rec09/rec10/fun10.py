def reduceListByN(lista,amount):
    '''
    This function takes a list and
    reduces the size of the list by a
    passed in amount.
    '''
    if amount<1:
        print "The number must be greater  or equal to one."
    else:
        for number in range(amount):
            lista.remove(lista[len(lista)])
            
