#!C:\Python27\python.exe

'''
cs1114

Submission:hw02

Programmer: Beihong Chen
Programmer username: bchen13
e of program: This is the module used to draw different kind of box
Constratints:
The output is alwyas displayed from left to right and from top to bottom.
'''

#These following is just an example to show the variables
#which are going to use in the program.
#However, these variables will be decided by caller, and
#they will never show in this module but in the main program.

#nameOfStr = "Johnny Aardvark"
'''
This is the string in the box
'''
#usingCharacter = "!"
'''
This is the chracter used in filling line.
'''
#fillingCharacter = "!"
'''
This is the chracter used in filling space.
'''
#spaceBetweenStr = 5
'''
This is the number of spaces between string and the box in each side.
'''
#numOfCharacter = len(nameOfStr) + (spaceBetweenStr * 2) +2
'''
This is the length of the line with chracter.
'''

def drawLineWithCharacter(usingCharacter,numOfCharacter):
    print usingCharacter * numOfCharacter

def drawSecAndForthLine(usingCharacter,numOfCharacter,fillingCharacter):
    print usingCharacter + (numOfCharacter-2)*fillingCharacter+usingCharacter

def drawLineWithString(usingCharacter,spaceBetweenStr,fillingCharacter,nameOfStr):
    print usingCharacter + spaceBetweenStr * fillingCharacter + nameOfStr + spaceBetweenStr * fillingCharacter + usingCharacter
