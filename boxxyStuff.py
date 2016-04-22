#!C:\Python27\pyhthon.exe

'''
cs1114

Submission:hw02

Programmer: Beihong Chen
Programmer username: bchen13
e of program: This is the module used to draw different kind of box
Constratints:
The output is alwyas displayed from left to right and from top to bottom.
'''

import lineOcharStuff

def drawFirstLine():
    '''
    This is the function to print first line.
    '''
    lineOcharStuff.drawLineWithCharacter(usingCharacter,numOfCharacter)


def drawSecLine():
    '''
    This is the function to print second line.
    '''
    lineOcharStuff.drawSecAndForthLine(usingCharacter,numOfCharacter,fillingCharacter)

def drawThirdLine():
    '''
    This is the function to print third line.
    '''
    drawLineWithString(usingCharacter,spaceBetweenStr,fillingCharacter,nameOfStr)

def drawForthLine():
    '''
    This is the function to print forth line.
    '''
    lineOcharStuff.drawSecAndForthLine(usingCharacter,numOfCharacter,fillingCharacter)

def drawFifithLine():
    '''
    This is the function to print fifth line.
    '''
    drawLineWithCharacter(usingCharacter,numOfCharacter)

def drawTheBox():
    '''
    This is the function to print the box.
    '''
    drawFirstLine()
    drawSecLine()
    drawThirdLine()
    drawForthLine()
    drawFifithLine()
