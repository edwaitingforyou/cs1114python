import prizeStuff
import random
KEY_WORD = "startrun"
SEVN_STAMP_AMOUNT = 100
THREE_STAMP_AMOUNT = 100
SIX_STAMP_AMOUNT = 100
DOLLARS_COIN = 100
QUARTERS_COIN = 100
DIMES_COIN = 100
NICKLES_COIN = 100
PENNIES_COIN = 100

def welcomeState():
    '''
    This function prints the welcome screen
    '''
    
    print '''
 --------------------------------------------
|     Welcome to the snakeStamp Machine!     |
| We dispense only 74, 32 and 6 cent stamps. |
| We give only coins in change - (no bills). |
 --------------------------------------------
'''

def getInfoFromUser():
    '''
    This function gets name from user.
    '''
    
    firstName = raw_input("What is your first name?")
    lastName = raw_input("What is your last name?")
    return firstName,lastName

def getStampFromUser():
    '''
    This function gets the amount of stamp of user
    '''
    sevenCentStamp = int(raw_input("How many 74 cent stamps would you like?"))
    threeCentStamp = int(raw_input("How many 32 cent stamps would you like?"))
    sixCentStamp = int(raw_input("How many 6 cent stamps would you like?"))
    return sevenCentStamp,threeCentStamp,sixCentStamp

def calcStamp(sevenCentStamp, threeCentStamp,sixCentStamp):
    '''
    This function calculates the price and amount
    of stamps that the user wants.
    '''

    stampAmount = sevenCentStamp + threeCentStamp + sixCentStamp
    stampPrice = 0.74*sevenCentStamp + threeCentStamp*0.32 + sixCentStamp*0.6
    return stampAmount,stampPrice

def printStamp(stampAmount,stampPrice):
    '''
    This function prints the price and amount
    of stamps for each user.
    '''

    print "The price of your", stampAmount, "stamps is $"+str(stampPrice)

def dollarFromUser():
    '''
    This function gets the number of dollars from users.
    '''

    userDollar = int(raw_input("How many dollars will you be giving us?"))
    return userDollar

def thanksScreen():
    '''
    This function prints the pause screen when
    the user finish all the input.
    '''

    print '''
Thank you. Just a moment please...
'''

def calTheAmtOfCoins(userDollar,stampPrice):
    '''
    This function will calculate the amount of
    each coins should be returned to user

    '''

    numOfDollars = int(userDollar - stampPrice)
    digitPart = float(userDollar) - float(stampPrice) - float(numOfDollars)
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

def printChange(numOfDollars, numOfQuaters, numOfDimes, numOfNickle, numOfPennes, firstName, lastName):
    '''
    This function print the change that the user
    is supposed to get.
    '''

    print "Thanks",firstName, lastName,"your change is:"
    if numOfDollars > 1:
        print numOfDollars, "dollar coins"
    elif numOfDollars == 1:
        print numOfDollars, "dollar coin"
    if numOfQuaters > 1:
        print numOfQuaters, "quarters"
    elif numOfQuaters == 1:
        print numOfQuaters, "quarter"
    if numOfDimes > 1:
        print numOfDimes, "dimess"
    elif numOfDimes == 1:
        print numOfDimes, "dime"
    if numOfNickle > 1:
        print numOfNickle, "nickels"
    elif numOfNickle == 1:
        print numOfNickle, "nickle"
    if numOfPennes > 1:
        print numOfPennes, "pennies"
    elif numOfPennes == 1:
        print numOfPennes, "penny"

def printThanks():
    '''
    This function prints thank in the last
    '''

    print '''
-======================================--
- Thank you for using our stamp machine -
-=======================================-
'''

def manageStep(numOfUser,numOfMoney,average,maxAmount,minAmount,perOfPrize):
    '''
    This function prints the statistics of the current
    situation of the machine to the manager.
    '''
    print "The number of user is", numOfUser
    print "The total money is", numOfMoney
    print "The average is", average
    print "The maximum is",maxAmount
    print "The minimun is",minAmount
    print "The percentage of prize is", str(perOfPrize*100)+"%"
    controlStatement = raw_input("Do you want to continue process?('Y'or'y'for yes, 'N'or'n'for no.")
    

def oneUser(firstName,lastName,numOfUser,numOfMoney):
    '''
    This function is all the processes with one user.
    '''
    sevenCentStamp,threeCentStamp,sixCentStamp = getStampFromUser()
    stampAmount,stampPrice = calcStamp(sevenCentStamp,threeCentStamp,sixCentStamp)
    printStamp(stampAmount,stampPrice)
    userDollar = dollarFromUser()
    numOfDollars, numOfQuaters, numOfDimes, numOfNickle, numOfPennes = calTheAmtOfCoins(userDollar,stampPrice)
    printChange(numOfDollars, numOfQuaters, numOfDimes, numOfNickle, numOfPennes, firstName, lastName)
    printThanks()
    return stampAmount,stampPrice,sevenCentStamp,threeCentStamp,sixCentStamp,userDollar,numOfDollars, numOfQuaters, numOfDimes, numOfNickle, numOfPennes
    

def main():
    sevenStampAmount = SEVN_STAMP_AMOUNT
    threeStampAmount = THREE_STAMP_AMOUNT
    sixStampAmount = SIX_STAMP_AMOUNT
    dollarsCoin = DOLLARS_COIN
    quartersCoin = QUARTERS_COIN
    dimesCoin = DIMES_COIN
    nicklesCoin = NICKLES_COIN
    penniesCoin = PENNIES_COIN
    numOfUser = 0
    numOfMoney = 0
    numOfPrize = 0
    maxAmount = 0
    minAmount = 10000000000
    while True and SEVN_STAMP_AMOUNT > 0\
          and THREE_STAMP_AMOUNT > 0 and SIX_STAMP_AMOUNT > 0\
          and DOLLARS_COIN > 0 and QUARTERS_COIN > 0\
          and DIMES_COIN > 0 and NICKLES_COIN and PENNIES_COIN > 0:
        welcomeState()
        firstName,lastName = getInfoFromUser()
        if firstName == "Iam" and lastName == "manager":break    
        stampAmount,stampPrice,userDollar,sevenCentStamp,threeCentStamp,sixCentStamp,numOfDollars, numOfQuaters, numOfDimes, numOfNickle, numOfPennes = oneUser(firstName,lastName,numOfUser,numOfMoney)
        numOfPrize += prizeStuff.givePrize(numOfQuaters,numOfDimes,numOfNickle,numOfPennes)
        if stampPrice > maxAmount:
            maxAmount = stampPrice
        if stampPrice < minAmount:
            minAmount = stampPrice
        numOfUser += 1
        numOfMoney += stampPrice
        average = numOfMoney/numOfUser
        perOfPrize = float(numOfPrize)/float(numOfUser)
        sevenStampAmount -= sevenCentStamp
        threeStampAmount -= threeCentStamp
        sixStampAmount -= sixCentStamp
        dollarsCoin -= numOfDollars
        dollarsCoin += userDollar
        quartersCoin -= numOfQuaters
        dimesCoin -= numOfDimes
        nicklesCoin -= numOfNickle
        penniesCoin -= numOfPennes
    manageStep(numOfUser,numOfMoney,average,maxAmount,minAmount,perOfPrize)

main()
