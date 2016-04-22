#!C:\Python27\python.exe
'''
This program is used to make a name box.
The programmer is Beihong Chen.
'''

import os

WIDTH_OF_BOX = 49
VALUE_OF_SPACE = 22

def main():
    drawLineOfX()
    drawBlankLine()
    drawLineOfName()
    drawBlankLine()
    drawLineOfX()

def drawLineOfX():
    '''
This function is for drawing the x line
'''
    print "x" * WIDTH_OF_BOX

def drawBlankLine():
    '''
This function is for drawing the blank line of the box.
'''
    print "x"," " * VALUE_OF_SPACE, " " * VALUE_OF_SPACE,"x"

def drawLineOfName():
    '''
This function is for drawing the name line'''
    
    print "x"," " * (VALUE_OF_SPACE - 6), "BeihongChen"," " * (VALUE_OF_SPACE -6),"x"

main()
if __name__ == '__main__':
    os.system("pause")
