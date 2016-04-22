#!C:\Pyhthon27\pyhthon.exe
#!C:\Python26\python.exe
'''
cs1114

Submission: rec03

Programmer: Beihong Chen
Username: bchen13
e of program:
This program make a bill of a coffee and daughnut shop.

Constratints:
The output is alwyas displayed from left to right and from top to bottom.

'''

import os
import rec04
import random

def requestOrder():
    '''
This function is used to get the amount of coffee and doughnuts the consumers need.
'''

    numOfCoffee = int(raw_input("How many coffee you need :"))
    numOfDaugh = int(raw_input("How many doughnuts you need :"))

    return numOfCoffee, numOfDaugh

def calculatePrice(numOfCoffee, numOfDaugh):
    '''
This function is used to calculate of coffee and doughnuts
'''
    costOfCoffee = 0.77
    costOfDaugh = 0.64
    priceOfCoffee = numOfCoffee * costOfCoffee
    priceOfDaugh = numOfDaugh * costOfDaugh

    return priceOfCoffee, priceOfDaugh

def calculateTax(priceOfCoffee, priceOfDaugh):
    '''
This function is used to calculate the tax the consumers need to pay.'''

    randomNum = -random.random()+1
    tax = 0.0846
    billBeforeTax = priceOfCoffee + priceOfDaugh
    taxOfBill = tax * billBeforeTax
    billAfterTax = billBeforeTax + (taxOfBill * randomNum)

    return billBeforeTax, billAfterTax, taxOfBill


def printbill(numOfCoffee, numOfDaugh, priceOfCoffee, priceOfDaugh, billBeforeTax, billAfterTax, taxOfBill):

    print'''

/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

THE COFFEE AND DOUGHNUT SHOPPE
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
'''
    print numOfCoffee, "cups of coffee: $",priceOfCoffee
    print numOfDaugh, "cups of daugh: $",priceOfDaugh

    print "==============================="
    print "Purchase amount: $%.2f" % billBeforeTax
    print "The tax is: $%.2f" % taxOfBill
    print "The bill added tax is:  $%.2f" % billAfterTax
    print "==============================="
    print "Thank you"
    rec04.calTheAmtOfCoins(billAfterTax)
    rec04.printAsCoins(billAfterTax)
    print "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ "
    numOfSegment = random.randint(4,6)
    randomNum = random.randint(0,1)
    print chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment * randomNum + (30 - numOfSegment * (4+randomNum)) * random.choice('12343567890<>~`!@#$%^&*:";')
    print chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment * randomNum + (30 - numOfSegment * (4+randomNum)) * random.choice('12343567890<>~`!@#$%^&*:";')
    print chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment + chr(random.randint(97,122)) * numOfSegment * randomNum + (30 - numOfSegment * (4+randomNum)) * random.choice('12343567890<>~`!@#$%^&*:";')
    print "/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ "

def main():
    numOfCoffee, numOfDaugh = requestOrder()
    priceOfCoffee, priceOfDaugh = calculatePrice(numOfCoffee, numOfDaugh)
    billBeforeTax, billAfterTax, taxOfBill = calculateTax(priceOfCoffee, priceOfDaugh)

    printbill(numOfCoffee, numOfDaugh, priceOfCoffee, priceOfDaugh, billBeforeTax, billAfterTax, taxOfBill)


main()
os.system("pause")


