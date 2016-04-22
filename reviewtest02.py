def getName():
    '''
    This function gets users'names
    '''
    name = raw_input("Enter your name:")
    return name

def addInput():
    '''
    This function gets numbers from user.
    '''
    lista = []
    numOfValue = int(raw_input("How many values will you enter:"))
    print "Enter your values, one per line:"
    for num in range(numOfValue):
        num = int(raw_input())
        lista += [num]
    return lista

def calSum(lista):
    '''
    This function calculates the sum of input.
    '''
    total = 0
    for num in lista:
        total += num
    return total

def printCredit(name):
    '''
    This function prints credits after inputing.
    '''
    print "Thank you",name+", processing will now begin..."

def printResult(lista,total):
    '''
    This function prints the result of sum calcuation.
    '''
    print "The sum of your",numOfValue,"values:"
    for num in lista:
        print num,
    print "is",total
