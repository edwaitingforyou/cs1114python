def givePrize(dollars, quarters, dimes, pennies):
    '''
    This function calculates which prize the consumer gets.
    '''
    grand = "Wow! You get the GRAND PRIZE!!!! It is $4,200,447.28!!!"
    second = "Cong.! You get the second prize! You get a T-shirt"
    third = "Cong.! You get the third prize! You get $10!"
    consolation = "Thank you and here is 2 cents as a gift!"
    if dollars == 1 and quarters == 0 and dimes == 1 and pennies == 3:
        print grand
        return 1
    elif (dollars == 2 and quarters == 2 and dimes == 0 and pennies == 4)\
         or (dollars == 3 and quarters == 0 and dimes == 0 and pennies == 2):
        print second
        return 1
    elif (dollars == 0 and quarters == 1 and dimes == 0 and pennies == 1)\
         or dimes in range(3,8):
        print third
        return 1
    else:
        return 0
