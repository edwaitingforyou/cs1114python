def printList(lista):
    '''
    This function displays items in a list.
    '''
    num = 1
    for items in lista:
        print num,":",items
        num += 1
        print "---------"

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

def main():
    lista = getList()
    printList(lista)

main()
