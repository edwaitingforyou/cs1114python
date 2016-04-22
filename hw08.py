#!C:\Python27\python.exe

def openTheFile():
    '''
    This function open files that cotains summary data
    extracted from a file of data about world population change.
    '''
    openFile = open("statistics","r")
    openFile.readline()
    oneLine = openFile.realine()

def dealWithTheFile(oneLine):
    '''
    This function deals with files that cotains summary data
    extracted from a file of data about world population change.
    The data is speared into two list by different period.
    '''
    newLine = oneLine.strip(",")
    lineList = newLine.split("\t")
    nameOfCountry = lineList[0]
    nameOfTerm = lineList[1]
    rateOfIncrease = lineList[2]
    theList = [nameOfCountry, nameOfTerm, rateOfChange]
    if nameOfTerm == "1970-1990":
        firstList.append(theList)
    else:
        secondList.append(theList)

def dealWithTheList(newList):
    '''
    This function deals with two lists we just got.
    The average, largest and smallest are calculated.
    '''

    
    totalRate = 0
    for item in newList:
        rate = float(item[1].strip("%"))
        countForOne += 1
        totalRate += rate
        item.reverse()
    averageRate = totalRate/countForOne
    newList.sort()
    largestRate1 = newList[0][0]
    largestRate2 = newList[1][1]
    largestRate3 = newList[2][2]
    newList.reverse()
    smallestRate1 = newList[0][0]
    smallestRate2 = newList[1][1]
    smallestRate3 = newList[2][2]
    return largestRate1,largestCountry1,smallestRate1,smallestCountry1,\
           largestRate2,largestCountry2,smallestRate2,smallestCountry2,\
           largestRate3,largestCountry3,smallestRate3,smallestCountry3,\
           averageRate
        

def creatTwoNewFilesAndStartToRead():
    '''
    This function creats with two empty files we will use to write data in.
    '''
    newFileOne = open("1970_1990_summary.txt","w")
    newFileTwo = open("1990_2007_summary.txt","w")
    return newFileOne,newFileTwo

def writeDataIntoNewFileOne(largestRateFirst1,largestCountryFirst1,smallestRateFirst1,smallestCountryFirst1,\
                      largestRateFirst2,largestCountryFirst2,smallestRateFirst2,smallestCountryFirst2,\
                      largestRateFirst3,largestCountryFirst3,smallestRateFirst3,smallestCountryFirst3,\
                      averageRateFirst):
    '''
    This function writes data into file of period 1970-1990.
    '''
    newFileOne = open("1970_1990_summary.txt","w")
    newFileOne.write("1970-1990 Summary Report\naverage growth over all countries: %.3f\nThe three ountries with largest growth:%s(%.2f), %s(%.2f), %s(%.2f)\nThe three countries with smallest growth:\n%s(%.2f), %s(%.2f), %s(%.2f)"%(averageRateOne,largestRateFirst1,largestCountryFirst1,largestRateFirst2,largestCountryFirst2,largestRateFirst3,largestCountryFirst3, smallestRateFirst1,smallestCountryFirst1,smallestRateFirst2,smallestCountryFirst2,smallestRateFirst3,smallestCountryFirst3))
    newLifeOne.close()

def writeDataIntoNewFileTwo(largestRateSecond1,largestCountrySecond1,smallestRateSecond1,smallestCountrySecond1,\
                      largestRateSecond2,largestCountrySecond2,smallestRateSecond2,smallestCountrySecond2,\
                      largestRateSecond3,largestCountrySecond3,smallestRateSecond3,smallestCountrySecond3,\
                      averageRateSecond):
    '''
    This function writes data into file of period 1990-2007.
    '''
    newFileTwo = open("1990_2007_summary.txt","w")
    newFileTwo.write("1990-2007 Summary Report\naverage growth over all countries: %.3f\nThe three ountries with largest growth:%s(%.2f), %s(%.2f), %s(%.2f)\nThe three countries with smallest growth:\n%s(%.2f), %s(%.2f), %s(%.2f)"%(averageRateTwo,largestRateSecond1,largestCountrySecond1,largestRateSecond2,largestCountrySecond2,largestRateSecond3,largestCountrySecond3,smallestRateSecond1,smallestCountrySecond1,smallestRateSecond2,smallestCountrySecond2,smallestRateSecond3,smallestCountrySecond3))
    newLifeTwo.close()

def main():
    firstList = []
    secondList = []
    openFile,oneLine = openTheFile()
    while oneLine != "":
        dealWithTheFile(oneLine)
        oneLine = openFile.readline()
    openFile.close()
    largestRateFirst1,largestCountryFirst1,smallestRateFirst1,smallestCountryFirst1,\
                      largestRateFirst2,largestCountryFirst2,smallestRateFirst2,smallestCountryFirst2,\
                      largestRateFirst3,largestCountryFirst3,smallestRateFirst3,smallestCountryFirst3,\
                      averageRateFirst = dealWithTheList(firstList)
    largestRateSecond1,largestCountrySecond1,smallestRateSecond1,smallestCountrySecond1,\
                      largestRateSecond2,largestCountrySecond2,smallestRateSecond2,smallestCountrySecond2,\
                      largestRateSecond3,largestCountrySecond3,smallestRateSecond3,smallestCountrySecond3,\
                      averageRateSecond = dealWithTheList(secondList)
    writeDataIntoNewFileOne(largestRateFirst1,largestCountryFirst1,smallestRateFirst1,smallestCountryFirst1,\
                      largestRateFirst2,largestCountryFirst2,smallestRateFirst2,smallestCountryFirst2,\
                      largestRateFirst3,largestCountryFirst3,smallestRateFirst3,smallestCountryFirst3,\
                      averageRateFirst)
    writeDataIntoNewFileTwo(largestRateSecond1,largestCountrySecond1,smallestRateSecond1,smallestCountrySecond1,\
                      largestRateSecond2,largestCountrySecond2,smallestRateSecond2,smallestCountrySecond2,\
                      largestRateSecond3,largestCountrySecond3,smallestRateSecond3,smallestCountrySecond3,\
                      averageRateSecond)

if __name__ == "__main__":
                     main()
    
    
