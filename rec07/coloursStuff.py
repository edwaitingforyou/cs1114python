import random
def getColor():
    '''
    This fucntion returns the random color of Tshirts of 2nd prize.
    '''

    randomColor = random.randint(1,8)
    if randomColor == "1":
        color = "red"
        return color
    elif randomColor == "2":
        color = "orange"
        return color
    elif randomColor == "3":
        color = "yellow"
        return color
    elif randomColor == "4":
        color = "green"
        return color
    elif randomColor == "5":
        color = "blue"
        return color
    elif randomColor == "6":
        color = "indigo"
        return color
    elif randomColor == "7":
        color = "violet"
        return color
    else:
        color = "black"
        return color

