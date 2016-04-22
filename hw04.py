#!C:\Python27\python.exe

'''
cs1114

Submission: hw04

Programmer: Beihong Chen
Username: bchen13

This program is used to calculate the tuition for an undergraudate student
in BRINY-U of each semeseter which adds an input validation function to enforce
that No student is allowed to take more than 30 credits.


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

def main():
    printCredit()
    lastName,firstName = getNameFromUser()
    IdNumber,userGender,remCourse,numOfRemCourse,numOfRegCredit = getInfoFromUser()
    userTuition,userFee,userOwe = calculateBill(remCourse,numOfRemCourse,numOfRegCredit)
    printCredit()
    calculateBill(remCourse,numOfRemCourse,numOfRegCredit)
    printBill(lastName,firstName,IdNumber,userGender,userTuition,userFee,userOwe)

if __name__ == "__main__":
    main()
