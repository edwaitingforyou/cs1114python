#!C:\Python27\python.exe

'''
cs1114

Submission: hw07

Programmer: Beihong Chen
Username: bchen13
Purpose of program:
This program plays the Hit && Match game that
A "try" consists of the "house" getting a "hand"
and the player getting a "hand" and the player
trying to make correct guesses.
Constratints:
The output is alwyas displayed from left to right and from top to bottom.

'''

import random
def getDigitFromUser():
    '''
    This function gets user's digits
    in the game.
    '''
    leftDigit = int(raw_input("Enter digit for left position:"))
    middleDigit = int(raw_input("Enter digit for middle position:"))
    while middleDigit == leftDigit:
        print "Sorry try again, can't have any duplicates."
        middleDigit = int(raw_input("Enter digit for middle position:"))
    rightDigit = int(raw_input("Enter digit for right position:"))
    while rightDigit == leftDigit or rightDigit == middleDigit:
        print "Sorry try again, can't have any duplicates."
        rightDigit = int(raw_input("Enter digit for right position:"))
    listA = [leftDigit,middleDigit,rightDigit]
    return listA

def getHouseDigit():
    '''
    This function gets random house digit.
    '''
    lista = range(1,10)
    leftDigit = random.choice(lista)
    lista.remove(leftDigit)
    middleDigit = random.choice(lista)
    lista.remove(middleDigit)
    rightDigit = random.choice(lista)
    listB = [leftDigit,middleDigit,rightDigit]
    
    return listB

def printBonus():
    '''
    This function shows wheather the user
    gets bonus or not.
    '''
    print "CONGRATULATIONS!!!"
    print
    randomNum = random.randint(7,12)
    for count in range(1,randomNum+1):
        print "BONUS "*count
    for count in range(randomNum-1,0,-1):
        print "BONUS "*count
    
def getCompetition(listA,listB):
    '''
    This function compares the digits from user
    and "house".
    '''
    hits = 0
    matches = 0
    for index in range(3):
        try:
            listB.index(listA[index])
            matchFound = True
        except ValueError:
            matchFound = False
        try:
            [listB[index]].index(listA[index])
            hitsFound = True
        except ValueError:
            hitsFound = False
        if hitsFound:
            hits += 1
        if matchFound:
            matches +=1
    matches -= hits
    return hits, matches

def printResult(listA,listB,hits,matches):
    '''
    This function prints the Result of
    the match.
    '''

    print "--House:"
    print "Left:   ",listB[0]
    print "Middle: ",listB[1]
    print "Right:  ",listB[2]
    print
    print "--Yours:"
    print "Left:   ",listA[0]
    print "Middle: ",listA[1]
    print "Right:  ",listA[2]
    
    print "Hits:", hits
    print "Matches:", matches
    print

def playHitAndMatch():
    '''
    This function deals with one single
    user for the program.
    '''
   
    listA = getDigitFromUser()
    listB = getHouseDigit()
    hits, matches = getCompetition(listA,listB)
    printResult(listA,listB,hits,matches)
    if hits == 3:
        printBonus()
        
def main():
    while True:
        playHitAndMatch()


if __name__ == "__main__":
    main()
