def printList(lista):
    '''
    This function displays items in a list.
    '''
    num = 1
    if len(lista)<99999:
        listb = []
        for items in lista:
            listb.append(items)
        listb.sort()
        for items in listb:
            print num,":",items
            num +=1
            print "---------"
