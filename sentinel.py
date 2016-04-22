STOP_VAL = "QUIT"
def getAvgOfUserInputs():
    sumOfItems = 0
    numOfItems = 0
    dataItems = raw_input("Enter first value or QUIT to quit:")
    while dataItems.upper() != STOP_VAL:
        sumOfItems += int(dataItems)
        numOfItems += 1
        dataItems = raw_input("Enter next value or QUIT to quit:")
    if numOfItems == 0:
        return 0, numOfItems
    else:
        return float(sumOfItems)/numOfItems, numOfItems

def main():
    avg,qnt = getAvgOfUserInputs()
    print "The average of your %i input was %.3f" % (qnt, avg)

main()
