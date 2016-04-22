CANT_DIVIDE_BY_ZERO = "You can not divide a number by 0"
def divisible(num1, num2):
    '''
    This function returns the value to show wheather the the number can be evenly
    divided by another number or not.
    '''

    if num2 != 0:
        return num1 % num2 == 0
 
    else:
        return CANT_DIVIDE_BY_ZERO
