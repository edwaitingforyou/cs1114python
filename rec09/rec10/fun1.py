def getList():
    '''
    This function gets words from the user and
    returns them in a list.
    '''
    lista = []
    word = raw_input("Enter the word into list:")
    lista.append(word)
    while word != "ZEBRA":
        word = raw_input("Enter the word into list:")
        lista.append(word)
    lista.remove("ZEBRA")
    return lista

