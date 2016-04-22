import os
num_apple = 3
print "The amount of apples is", num_apple
priceOfApple = 5
print "The price of each apple is", priceOfApple
price = num_apple * priceOfApple
your_answer = int(raw_input('Enter your answer : '))
if your_answer == price:
    print "The total price of apple is 15. Congratulations!"
elif your_answer != price:
    print "The total price of apple is not your_answer. Please do it again!"
print "apple is good for your health"
