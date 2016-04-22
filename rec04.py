'''
This moduel deals with money conversion and printing.
'''

def printAsUsDollars(number, pref):
    '''
    This function is going print the
    right decimal digits we need.

    '''

    dollarsWith2Digit = round(number, 2)
    print pref + str(dollarsWith2Digit)

def convertPesosToUSDollars(amtOfPesos):
    '''
    This function is going to return
    the amount of US dollar from pesos.

    '''

    rateOfPesosToUSDollars = 0.0780
    usDollarsFromPesos = amtOfPesos * rateOfPesosToUsDollars


def calTheAmtOfCoins(usDollarsOfRightDigit):
    '''
    This function will calculate
    the amount of each coins

    '''

    numOfDollars = int(usDollarsOfRightDigit)
    digitPart = usDollarsOfRightDigit - int(usDollarsOfRightDigit)
    quatersNum = 4
    quatersPrice = 0.25
    numOfQuaters = int(digitPart * quatersNum)
    quatersAmt = quatersPrice * numOfQuaters
    dimesNum = 10
    dimesPrice = 0.10
    numOfDimes = int((digitPart - quatersAmt) * dimesNum)
    dimesAmt = dimesPrice * numOfDimes
    nickleNum = 20
    nicklePrice = 0.05
    numOfNickle = int((digitPart - quatersAmt - dimesAmt) * nickleNum)
    nickleAmt = nicklePrice * numOfNickle
    pennesNum = 100
    numOfPennes = int((digitPart - quatersAmt - dimesAmt - nickleAmt) * pennesNum)

    return numOfDollars, numOfQuaters, numOfDimes, numOfNickle, numOfPennes

def printAsCoins(usDollarsOfRightDigit):
    '''
    This function will tell the user
    the amount of each coins

    '''

    numOfDollars, numOfQuaters, numOfDimes, numOfNickle, numOfPennes = calTheAmtOfCoins(usDollarsOfRightDigit)
    print "Dollars", numOfDollars
    print "Quaters", numOfQuaters
    print "Dimes", numOfDimes
    print "Nickles", numOfNickle
    print "Pennes", numOfPennes
