import os
def main():
    drawLine1()
    drawLine2()
    drawLine1()
print "The program is used to make your name look better, the line will be distrubuted by 'x'."
print "By the way, if width of the box = the space you want * 2 + 41, the box will stay in the best style."
Width_of_box = int(raw_input('Enter the width of the box : '))
Value_of_space = int(raw_input('Enter the space you need before and after your name : '))
def drawLine1():
    print "x" * Width_of_box
    print "x" * Width_of_box
def drawLine2():
    print "xx"," " * Value_of_space, "@@@@@@    @@@@@@   @@@@@   @    @"," " * Value_of_space,"xx"
    print "xx"," " * Value_of_space, "@    @    @          @     @    @"," " * Value_of_space,"xx"
    print "xx"," " * Value_of_space, "@   @     @          @     @    @"," " * Value_of_space,"xx"
    print "xx"," " * Value_of_space, "@@@@      @@@@@      @     @@@@@@"," " * Value_of_space,"xx"
    print "xx"," " * Value_of_space, "@   @     @          @     @    @"," " * Value_of_space,"xx"
    print "xx"," " * Value_of_space, "@    @    @          @     @    @"," " * Value_of_space,"xx"
    print "xx"," " * Value_of_space, "@@@@@@    @@@@@@   @@@@@   @    @"," " * Value_of_space,"xx"

main()
if main():
    os.system("pause")
