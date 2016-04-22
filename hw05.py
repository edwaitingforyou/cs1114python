#!C:\Python27\python.exe

'''
cs1114

Submission: hw04

Programmer: Beihong Chen
Username: bchen13

This program is used to calculate the tuition for an undergraudate student
in BRINY-U of each semeseter which adds an input validation function to enforce
that No student is allowed to take more than 30 credits. A loop to calculate for
many students and a manager process is included.


Constratints:
The output is always displayed from left to right and from top to bottom.
'''

def getNameFromUser():
    '''
    This function is used to get name from the user.
    '''
    
    lastName = raw_input("Enter your last name: ")
    firstName = raw_input("Enter your first name: ")   
    return lastName,firstName

def getInfoFromUser():
    '''
    This function is used to get information of the user.
    '''
    IdNumber = int(raw_input("Enter your BRINY-U numer(without any leading zero): "))
    userGender = raw_input("Enter your gender ('M' for male and 'F' for female):")
    remCourse = raw_input("Are you taking any remedial courses? (enter Y for yes and N for no):")
    if remCourse.upper() == "Y":
        numOfRemCourse = int(raw_input("Enter the number of remedial courses that you are taking: "))
    elif remCourse.upper() == "N":
        numOfRemCourse = 0
    numOfRegCredit = int(raw_input("Enter the number of regular credits you are taking: "))
    while numOfRegCredit > 30 or numOfRegCredit <= 0:
        print "Sorry, try again."
        numOfRegCredit = int(raw_input("Enter the number of regular credits you are taking: "))
    return IdNumber,userGender,remCourse,numOfRemCourse,numOfRegCredit
     
def printCredit():
    '''
    This function is used to print cerdits on the screen
    in the beginning of the program and bewteen user's information and bill
    '''

    print '''
BRBRBR-------------BRBRBR
BRBRBR   BRINY-U   BRBRBR
BRBRBR-------------BRBRBR
'''

def calculateBill(remCourse,numOfRemCourse,numOfRegCredit):
    '''
    This function is used to calculate the tuition and fee for the student.
    '''

    if numOfRegCredit >= 12 and numOfRegCredit <= 20:
        userTuition = 14000 + numOfRemCourse * 3000
    elif numOfRegCredit > 20:
        userTuition = 14000 + 800 * (numOfRegCredit - 20) + numOfRemCourse * 3000
    else:
        userTuition = 900 * numOfRegCredit + numOfRemCourse * 3000

    userFee = 100+30*(numOfRegCredit + numOfRemCourse)
    userOwe = userFee + userTuition
    return userTuition,userFee,userOwe

def printBill(lastName,firstName,IdNumber,userGender,userTuition,userFee,userOwe):
    '''
    This function is used to print the student's bill.
    '''

    if userGender.upper() == "M":
        printGender = "Mr."
    elif userGender.upper() == "F":
        printGender = "Ms."

    print printGender, lastName, firstName, "(" + str(IdNumber) + ")"
    print "Your tuition is:", userTuition
    print "Your fee is:", userFee
    print "You owe:", userOwe

def endProcess(totalUser,totalOwe,average,maxOwe,minOwe,malePercentage,femalePercentage):
    '''
    This function is the process when the user ends the program.
    '''
    print str(totalUser), "students are registered meaning we'll be getting $"+str(totalOwe)
    print "The average amount owed is $"+str(average)
    print "The largest amount owed by any student is $"+str(maxOwe)
    print "The smallest amount owed by any student is $"+str(minOwe)
    print "There were", malePercentage*100,"% males and",femalePercentage*100,"% females."
    

def oneStudent(lastName,firstName):
    '''
    This function is the total process of one student with given
    lastName and firstName.
    '''
    
    IdNumber,userGender,remCourse,numOfRemCourse,numOfRegCredit = getInfoFromUser()
    userTuition,userFee,userOwe = calculateBill(remCourse,numOfRemCourse,numOfRegCredit)
    printCredit()
    printBill(lastName,firstName,IdNumber,userGender,userTuition,userFee,userOwe)
    return remCourse,numOfRemCourse,numOfRegCredit,userGender,userOwe

def main():
    totalOwe = 0
    totalUser = 0
    numOfMale = 0
    numOfFemale = 0
    maxOwe = 0
    minOwe = 10000000000000000000
    averageCost = 0
    malePercentage = 0
    femalePercentage = 0
    while True:
        printCredit()
        lastName,firstName = getNameFromUser()
        if firstName == "END OF PROCESSING":break
        remCourse,numOfRemCourse,numOfRegCredit,userGender,userOwe = oneStudent(lastName,firstName)
        if userGender.upper() == "M":
            numOfMale += 1
        elif userGender.upper() == "F":
            numOfFemale += 1
        totalUser += 1
        totalOwe += userOwe
        averageCost = float(totalOwe) / float(totalUser)
        malePercentage = float(numOfMale) / float(totalUser)
        femalePercentage = float(numOfFemale) / float(totalUser)
        if userOwe < minOwe:
            minOwe = userOwe
        if userOwe > maxOwe:
            maxOwe = userOwe
    endProcess(totalUser,totalOwe,averageCost,maxOwe,minOwe,malePercentage,femalePercentage)

if __name__ == "__main__":
    main()
    
