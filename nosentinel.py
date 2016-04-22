def getAvgOfUserInputs():
    sumOfItems = 0
    numOfItems = 0
    numOfItems = int(raw_input("Enter # of value :"))
    for itemNumber in range(numOfItems):
        dataItems = raw_input("Enter a value:")
        sumOfItems += float(dataItems)        
    if numOfItems == 0:
        return 0, numOfItems
    else:
        return sumOfItems/numOfItems, numOfItems

def main():
    avg,qnt = getAvgOfUserInputs()
    print "The average of your %i input was %.3f" % (qnt, avg)

main()
