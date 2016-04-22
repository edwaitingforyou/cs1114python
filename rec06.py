def prinLine(first,sec,third):
    import random
    if first, sec, third:
        line = first*random.randint(3,17)+sec*random.randint(5,22)+third*random.randint(2,14)
    elif first,sec:
        line = first*random.randint(3,17)+sec*random.randint(5,22)+"Z"*random.randint(2,14)
    elif first:
        line = first*random.randint(3,17)+"Y"*random.randint(5,22)+"Z"*random.randint(2,14)
    else:
        line = "X"*random.randint(3,17)+"Y"*random.randint(5,22)+"Z"*random.randint(2,14)
    print line  


prinLine(A)
