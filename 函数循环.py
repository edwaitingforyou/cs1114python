#!C:\Python27\python.exe

'''
This is the program to practice function's connection
Programmer: Beihong Chen
'''

import os
def main():
    startup_message()
    raw_input('Press enter to see step 1.')
    step1()
    raw_input('Press enter to see step 2.')
    step2()
    running = True
    while running:
        print 'If you do not want to be an idiot please follow the instruction and go back to step 1.'
        your_answer = str(raw_input("Enter 'I am idoit' : "))
        answer_run = 'I am idoit'
        if your_answer == answer_run:
            print 'I know you are the most stupid guy,whatever, the test is done! Cong. idiot!'
            os.system("pause")
            running = False
        elif your_answer != answer_run:
            step3()
            running = True

def startup_message():
    print 'This program tells you how to become an idiot. Whatever, lets start to become an idiot!'
def step1():
    print 'If you think you are not an idiot, follow the step.'
def step2():
    print 'Now you are in my quantao! Enjoy idoit!'
def step3():
    print 'Hey idoit why not follow my instruction, you are now a 100% idoit!'
    
main()
