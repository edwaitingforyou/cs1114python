#!C:\Python27\python.exe

'''
cs1114

Submission: hw01

Programmer: Beihong Chen
Username: bchen13
Purpose of program:
Draw a box around the user's first name and another
around the user's last name then pause the screen with
your credits/pause showing.
Constratints:
The output is alwyas displayed from left to right and from top to bottom.

'''

import os
import getUserInfo
import drawBoxWithX
import printCredits


os.system("cls")
'''
We are told to only def main function, so these part
will be blank for the sub functions
'''

def main():
    userFirstName, userLastName = getUserInfo.getUserName()
    spaceBetweenStr = 2
    '''
    getUserName()is the function to get
    user's fistname and lastname by str(raw_input("What is your first name?"))
    and str(raw_input("What is your last name?"))
    '''
    
    #The following subfuction needs varible spaceInTheLine to calculate how many X in the line.
    draBoxWithX.drawLineWithX(userFirstName)
    draBoxWithX.drawLineWithSpaceAndX(userFirstName)
    draBoxWithX.drawLineAndStr(userFirstName)
    draBoxWithX.drawLineWithSpaceAndX(userFirstName)
    draBoxWithX.drawLineWithX(userFirstName)
    '''
    The caller uses len(userFirstName) and the spaceInTheLine
    to calculate how many X should be used in each line
    Also the space will be counted.
    '''

    #The following subfuction needs varible spaceInTheLine to calculate how many X in the line.
    draBoxWithX.drawLineWithX(userLastName)
    draBoxWithX.drawLineWithSpaceAndX(userLastName)
    draBoxWithX.drawLineAndStr(userLastName)
    draBoxWithX.drawLineWithSpaceAndX(userLastName)
    draBoxWithX.drawLineWithX(userLastName)
    '''
    The caller uses len(userFirstName) and the spaceInTheLine
    to calculate how many X should be used in each line
    Also the space will be counted.
    '''

    printCredits.printCredits()
    '''
    This function prints programmer's credits.
    '''

main()
if __name__ == '__main__':
    os.system("pause")



