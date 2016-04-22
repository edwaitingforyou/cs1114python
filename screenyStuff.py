#!C:\Python27\python.exe

'''
cs1114

Submission:hw02

Programmer:Beihong Chen
Programmer username: bchen13
This module is used to clean the screen
and pasue the screen by importing os.
Constratints:
The output is alwyas displayed from left to right and from top to bottom.
'''

import os

def pauseTheScreen():
    '''This function is used to pause the screen.'''
    os.system("pause")

def cleanTheScreen():
    '''This function is used to clean thescreen.'''
    os.system("cls")
