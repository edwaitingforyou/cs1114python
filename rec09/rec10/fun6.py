import random
def addFucntion(lista,listb):
    '''
    This function take two lists and
    produce a list with an item randomly chosen
    from the first list stuck into the second list
    somewhere between some pair of items.
    '''
    listb.insert(random.randint(0,len(listb)),randon.choice(lista))
    return newList
