# -*- coding: cp936 -*-
import math
import os

p = math.pi

def calCos(x):
    cos = math.cos(x)
    return cos
def calSin(x):
    sin = math.sin(x)
    return sin
def calTan(x):
    tan = math.tan(x)
    return tan

def getX():
    xbyuser = eval(raw_input("请输入:"))
    return xbyuser

def printCos(cos):
    if cos < 0.000000000001 and cos > 0 or cos > -0.000000000001 and cos <0:
        print "cos",0
    else:
        print "cos",cos

def printSin(sin):
    if sin < 0.000000000001 and sin > 0 or sin > -0.000000000001 and sin <0:
        print "sin",0
    else:
        print "sin",sin

def printTan(tan):
    if tan < 0.000000000001 and tan > 0 or tan > -0.000000000001 and tan <0:
        print "tan",0
    elif tan > 100000000 or tan < -0.00000000000001:
        print "tan doesn't exsit"
    else:
        print "tan",tan

def printSec(cos):
    if 1/cos < 0.000000000001 and 1/cos > 0 or 1/cos > -0.000000000001 and 1/cos <0:
        print "sec",0
    elif 1/cos > 10000000000:
        print "sec doesn't exsit"
    else:
        print "sec",1/cos

def printCsc(sin):
    if 1/sin < 0.000000000001 and 1/sin > 0 or 1/sin > -0.000000000001 and 1/sin <0:
        print "csc",0
    elif 1/sin > 10000000000:
        print "csc doesn't exsit"
    else:
        print "csc",1/sin

def printCot(tan):
    if 1/tan < 0.000000000001 and 1/tan > 0 or 1/tan > -0.000000000001 and 1/tan <0:
        print "cot",0
    elif 1/tan > 10000000000:
        print "cot doesn't exsit"
    else:
        print "cot",1/tan

def printCredits():
    print "Please record your results as soon as possbile"
    print "The program will close after entering any button."
    os.system("pause")

def printUserInfo():
    print "请用'p'代替pi圆周率，如果我要输入3pi，即输入3*p"
    
def main():
    x = getX()
    cos = calCos(x)
    sin = calSin(x)
    tan = calTan(x)
    printUserInfo()
    printSin(sin)
    printCos(cos)
    printTan(tan)
    printSec(sin)
    printCsc(cos)
    printCot(tan)
    printCredits()


main()
