#!C:\Python27\python.exe

def openTheFile():
    '''
    This function open files that cotains summary data
    extracted from a file of data about world population change.
    '''
    openFile = open("statistics.txt","r")
    oneLine = openFile.readline()
    oneLine = openFile.readline()
    return openFile,oneLine

def dealWithTheFile(oneLine,firstList,secondList):
    '''
    This function deals with files that cotains summary data
    extracted from a file of data about world population change.
    The data is speared into two list by different period.
    '''
    newLine = oneLine.replace(", ","\t")
    newLine2 = newLine.strip("\n")
    lineList = newLine2.split("\t")
    nameOfCountry = lineList[0]
    nameOfTerm = lineList[1]
    rateOfIncrease = lineList[2]
    theList = [nameOfCountry, rateOfIncrease]
    if nameOfTerm == "1970-1990":
        firstList.append(theList)
    else:
        secondList.append(theList)

def dealWithTheList(newList):
    '''
    This function deals with two lists we just got.
    The average, largest and smallest are calculated.
    '''

    countForOne = 0
    totalRate = 0
    for item in newList:
        rate = float(item[1].replace("%","0"))
        item[1]=rate
        countForOne += 1
        totalRate += rate
        item.reverse()
    averageRate = totalRate/countForOne
    newList.sort()
    smallestRate1 = newList[0][0]
    smallestRate2 = newList[1][0]
    smallestRate3 = newList[2][0]
    smallestCountry1 = newList[0][1]
    smallestCountry2 = newList[1][1]
    smallestCountry3 = newList[2][1]
    newList.reverse()
    largestRate1 = newList[0][0]
    largestRate2 = newList[1][0]
    largestRate3 = newList[2][0]
    largestCountry1 = newList[0][1]
    largestCountry2 = newList[1][1]
    largestCountry3 = newList[2][1]
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



def writeDataIntoNewFile(largestRateSecond1,largestCountrySecond1,smallestRateSecond1,smallestCountrySecond1,\
                      largestRateSecond2,largestCountrySecond2,smallestRateSecond2,smallestCountrySecond2,\
                      largestRateSecond3,largestCountrySecond3,smallestRateSecond3,smallestCountrySecond3,\
                      averageRateSecond,period):
    '''
    This function writes data into files.
    '''
    if period == 1:
         newFileOne = open("1970_1990_summary.txt","w")
         newFileOne.write("1970-1990 Summary Report\naverage growth over all countries: %.3f%%\nThe three ountries with largest growth:\n%s(%.2f%%), %s(%.2f%%), %s(%.2f%%)\nThe three countries with smallest growth:\n%s(%.2f%%), %s(%.2f%%), %s(%.2f%%)"%(averageRateFirst,largestCountryFirst1,largestRateFirst1,largestCountryFirst2,largestRateFirst2,largestCountryFirst3,largestRateFirst3,smallestCountryFirst1,smallestRateFirst1,smallestCountryFirst2,smallestRateFirst2,smallestCountryFirst3,smallestRateFirst3))
         newFileOne.close()
    else:
        newFileTwo = open("1990_2007_summary.txt","w")
        newFileTwo.write("1990-2007 Summary Report\naverage growth over all countries: %.3f%%\nThe three ountries with largest growth:\n%s (%.2f%%), %s(%.2f%%), %s(%.2f%%)\nThe three countries with smallest growth:\n%s(%.2f%%), %s(%.2f%%), %s(%.2f%%)"%(averageRateSecond,largestCountrySecond1,largestRateSecond1,largestCountrySecond2,largestRateSecond2,largestCountrySecond3,largestRateSecond3,smallestCountrySecond1,smallestRateSecond1,smallestCountrySecond2,smallestRateSecond2,smallestCountrySecond3,smallestRateSecond3))
        newFileTwo.close()

def main():
    firstList = []
    secondList = []
    openFile,oneLine = openTheFile()
    while oneLine != "":
        dealWithTheFile(oneLine,firstList,secondList)
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
    writeDataIntoNewFile(largestRateFirst1,largestCountryFirst1,smallestRateFirst1,smallestCountryFirst1,\
                      largestRateFirst2,largestCountryFirst2,smallestRateFirst2,smallestCountryFirst2,\
                      largestRateFirst3,largestCountryFirst3,smallestRateFirst3,smallestCountryFirst3,\
                      averageRateFirst,period = 1)
    writeDataIntoNewFile(largestRateSecond1,largestCountrySecond1,smallestRateSecond1,smallestCountrySecond1,\
                      largestRateSecond2,largestCountrySecond2,smallestRateSecond2,smallestCountrySecond2,\
                      largestRateSecond3,largestCountrySecond3,smallestRateSecond3,smallestCountrySecond3,\
                      averageRateSecond,period = 2)

if __name__ == "__main__":
                     main()
    
    
