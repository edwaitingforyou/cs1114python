#!C:\Python27\python.exe
#This program is just for fun.
#I dont believe anyone will fail in this question.
#Don't believe there is a surprise.
#Copyright is free
#I am so boried because my girlfriend has soooooooooo many class and work to do and my JiYous are not going to play Dota.
#Let's start.
print "This is a question about primary school math."
print "This a primary school maths question which is so stupid that any one fail it should have taken my maths course for a while."
print "Let's start!"
import os
num_apple = int(raw_input('Enter a number whatever you like : '))
print "The amount of apples is", num_apple
priceOfApple = int(raw_input('Enter the price of one apple in your common science : '))
print "The price of each apple is", priceOfApple
price = num_apple * priceOfApple
running = True
while running:
    print "What is the total price of the apples?"
    your_answer = int(raw_input('Enter your answer : '))
    if your_answer != price:
        print "Sorry. Please do it again!"
        running = True

    elif your_answer == price:
        running = False
else:
    print "Cong. sweaty! Your are so cute!OvO"
    os.system("pause")
    
print "By the way. Apple is good for your health"
