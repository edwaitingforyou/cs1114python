ANTICLOCKWISE = 2
CLOCKWISE = 1

def rotateThese(var1, var2, var3, direct = CLOCKWISE):
    '''
    This function rotates the 3 parameters by clockwise or anti clockwise.
    '''

    if direct == 1:
        return var2, var3, var1
    else:
        return var3, var1, var2
